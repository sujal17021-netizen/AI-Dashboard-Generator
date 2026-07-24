# services/dataset_analyzer.py

import pandas as pd

from services.column_detector import detect_columns


def analyze_dataset(df: pd.DataFrame):

    """
    Analyze the uploaded dataset.

    Returns:
    - total rows
    - total columns
    - column names
    - dimensions
    - measures
    - dates
    """

    # --------------------------
    # Total rows
    # --------------------------

    total_rows = len(df)

    # --------------------------
    # Total columns
    # --------------------------

    total_columns = len(df.columns)

    # --------------------------
    # Column names
    # --------------------------

    column_names = list(df.columns)

    # --------------------------
    # Detect dimensions,
    # measures and dates
    # --------------------------

    column_information = detect_columns(df)

    dimensions = column_information["dimensions"]

    measures = column_information["measures"]

    dates = column_information["dates"]

    # --------------------------
    # Return everything
    # --------------------------

    return {

        "rows": total_rows,

        "columns": total_columns,

        "column_names": column_names,

        "dimensions": dimensions,

        "measures": measures,

        "dates": dates

    }