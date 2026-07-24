import pandas as pd
from fastapi import UploadFile
from sqlalchemy.orm import Session

from crud import (
    save_dataset,
    save_dataset_rows,
    get_dataset_by_hash,
)

from services.hashing import generate_dataset_hash


async def upload_dataset_service(
    file: UploadFile,
    db: Session
):
    """
    Upload dataset into database.
    Handles duplicate detection using dataset hash.
    """

    # -----------------------------------------
    # Read Excel
    # -----------------------------------------
    df = pd.read_excel(file.file)

    print("=" * 60)
    print(f"Rows in Excel : {len(df)}")
    print("=" * 60)

    # -----------------------------------------
    # Generate Dataset Hash
    # -----------------------------------------
    dataset_hash = generate_dataset_hash(df)

    print("=" * 60)
    print("Generated Hash :", dataset_hash)
    print("=" * 60)

    # -----------------------------------------
    # Check if dataset already exists
    # -----------------------------------------
    existing_dataset = get_dataset_by_hash(
        db=db,
        dataset_hash=dataset_hash
    )

    print("Existing Dataset :", existing_dataset)

    if existing_dataset is not None:

        print("=" * 60)
        print("Dataset already exists.")
        print("Using Dataset ID :", existing_dataset.id)
        print("=" * 60)

        return {
            "message": "Dataset already exists.",
            "dataset_id": existing_dataset.id,
            "rows": len(df)
        }

    # -----------------------------------------
    # Save Dataset
    # -----------------------------------------
    dataset = save_dataset(
        db=db,
        filename=file.filename,
        dataset_hash=dataset_hash
    )

    print("=" * 60)
    print("New Dataset Created")
    print("Dataset ID :", dataset.id)
    print("=" * 60)

    # -----------------------------------------
    # Save Dataset Rows
    # -----------------------------------------
    save_dataset_rows(
        db=db,
        dataset_id=dataset.id,
        dataframe=df
    )

    print("=" * 60)
    print("Rows inserted successfully.")
    print("=" * 60)

    return {
        "message": "Dataset uploaded successfully.",
        "dataset_id": dataset.id,
        "rows": len(df)
    }