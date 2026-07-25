from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
    HTTPException,
    Depends
)

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import traceback


# ==========================================
# DATABASE
# ==========================================

from database import get_db

from crud import (
    fetch_dataset
)


# ==========================================
# SERVICES
# ==========================================

from services.dataset_service import (
    upload_dataset_service
)

from services.prompt_classifier import (
    classify_prompt
)

from services.auto_dashboard import (
    generate_auto_dashboard
)


# ==========================================
# ROUTER
# ==========================================

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


# ==========================================
# UPLOAD DATASET
# ==========================================

@router.post("/upload")
async def upload_dataset(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:

        return await upload_dataset_service(
            file=file,
            db=db
        )

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# ==========================================
# GENERATE DASHBOARD
# ==========================================

# 
@router.post("/generate")
async def generate_dashboard(
    dataset_id: int = Form(...),
    prompt: str = Form(...),
    db: Session = Depends(get_db)
):
    print("GENERATE ROUTE REACHED")

    try:
        print("STEP 1")
        intent = classify_prompt(prompt)

        print("STEP 2")
        df = fetch_dataset(
            db=db,
            dataset_id=dataset_id
        )

        print("Rows:", len(df))

        print("STEP 3")
        dashboard = generate_auto_dashboard(df)

        print("STEP 4")

        return jsonable_encoder(dashboard)

    except Exception as e:
        print("========== ERROR ==========")
        print(e)
        traceback.print_exc()
        raise