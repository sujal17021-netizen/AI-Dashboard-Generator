from routes.dashboard import router as dashboard_router
from fastapi import FastAPI, UploadFile, File,Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
from io import BytesIO
import os
from dotenv import load_dotenv
from google import genai
from database import engine
from database import Base
from database import engine
from models import Base
from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from crud import save_uploaded_file

import models
Base.metadata.create_all(bind=engine)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# -----------------------------
# Global Data
# -----------------------------
uploaded_df = None

# -----------------------------
# Request Models
# -----------------------------
class FilterRequest(BaseModel):
    dimension: str
    measure: str
    filters: dict = {}

# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI()
app.include_router(dashboard_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://ai-dashboard-generator-six.vercel.app"
    ],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

# -----------------------------
# Home API
# -----------------------------
@app.get("/")
def home():
    return {"message": "Dashboard Backend is Running 🚀"}

# -----------------------------
# KPI Calculator
# -----------------------------
def calculate_kpis(df: pd.DataFrame):

    dimensions = list(df.select_dtypes(include=["object"]).columns)
    measures = list(df.select_dtypes(include=["number"]).columns)

    kpis = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "total_dimensions": len(dimensions),
        "total_measures": len(measures),
    }

    numeric_summary = {}

    for column in measures:

        # Remove NaN values
        series = pd.to_numeric(df[column], errors="coerce").dropna()

        if series.empty:

            numeric_summary[column] = {
                "sum": 0,
                "average": 0,
                "minimum": 0,
                "maximum": 0,
            }

        else:

            numeric_summary[column] = {
                "sum": round(float(series.sum()), 2),
                "average": round(float(series.mean()), 2),
                "minimum": round(float(series.min()), 2),
                "maximum": round(float(series.max()), 2),
            }

    kpis["numeric_summary"] = numeric_summary

    return kpis

def generate_ai_insights(df: pd.DataFrame):

    if df.empty:
        return "No data available for analysis."

    summary = df.describe(include="all").to_string()

    prompt = f"""
You are an expert Business Intelligence analyst.

Analyze the following dataset summary.

Give:

1. Key business insights
2. Trends
3. Anomalies
4. Recommendations

Dataset Summary:

{summary}

Return your answer as bullet points.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
# -----------------------------
# Upload Excel
# -----------------------------


# -----------------------------
# Get Filters
# -----------------------------
@app.get("/filters")
async def get_filters():

    global uploaded_df

    if uploaded_df is None:
        return {}

    filters = {}

    object_columns = uploaded_df.select_dtypes(
        include=["object"]
    ).columns

    for column in object_columns:

        filters[column] = sorted(
            uploaded_df[column]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

    return filters
# -----------------------------
# Generate Dashboard
# -----------------------------
@app.post("/generate-dashboard")
async def generate_dashboard(request: FilterRequest):

    global uploaded_df

    if uploaded_df is None:
        return {
            "error": "Please upload an Excel file first."
        }

    # Work on a copy
    df = uploaded_df.copy()

    # -----------------------------
    # Apply Filters
    # -----------------------------
    for column, value in request.filters.items():

        if value != "" and column in df.columns:

            df = df[df[column].astype(str) == str(value)]

    # -----------------------------
    # If no data after filtering
    # -----------------------------
    if df.empty:

        return {
            "chartData": [],
            "tableData": [],
            "kpis": calculate_kpis(df),
        }

    # -----------------------------
    # Validate Dimension & Measure
    # -----------------------------
    if request.dimension not in df.columns:
        return {
            "error": f"Dimension '{request.dimension}' not found."
        }

    if request.measure not in df.columns:
        return {
            "error": f"Measure '{request.measure}' not found."
        }

    # -----------------------------
    # Group Data
    # -----------------------------
    chart_df = (
        df.groupby(request.dimension)[request.measure]
        .sum()
        .reset_index()
    )

    # -----------------------------
    # Remove NaN / Infinity
    # -----------------------------
    chart_df = (
        chart_df
        .fillna(0)
        .replace([float("inf"), float("-inf")], 0)
    )

    table_df = (
        df
        .fillna("")
        .replace([float("inf"), float("-inf")], 0)
    )
    from fastapi import Form


@app.post("/generate-dashboard-ai")
async def generate_dashboard_ai(

    file: UploadFile = File(...),

    prompt: str = Form(...)

):

    return {

        "filename": file.filename,

        "prompt": prompt

    }

    # -----------------------------
    # Return Dashboard 
    # -----------------------------
       # -----------------------------
    # Return Dashboard
    # -----------------------------

    insights = generate_ai_insights(df)

    return {
        "chartData": chart_df.to_dict(orient="records"),
        "tableData": table_df.to_dict(orient="records"),
        "kpis": calculate_kpis(df),
        "insights": insights,
    }