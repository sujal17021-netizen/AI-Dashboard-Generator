import pandas as pd


DATE_KEYWORDS = [
    "date",
    "day",
    "month",
    "year",
    "time",
    "created",
    "updated",
]

ID_KEYWORDS = [
    "id",
    "code",
    "number",
    "no",
]

GEO_KEYWORDS = [
    "country",
    "state",
    "city",
    "region",
    "district",
    "location",
]


def detect_columns(df: pd.DataFrame):

    dimensions = []
    measures = []
    dates = []
    ids = []
    geo = []
    booleans = []

    for column in df.columns:

        col = column.lower()

        # -------------------------
        # Boolean
        # -------------------------
        if pd.api.types.is_bool_dtype(df[column]):
            booleans.append(column)
            continue

        # -------------------------
        # Datetime datatype
        # -------------------------
        if pd.api.types.is_datetime64_any_dtype(df[column]):
            dates.append(column)
            continue

        # -------------------------
        # Date by column name
        # -------------------------
        if any(word in col for word in DATE_KEYWORDS):
            dates.append(column)
            continue

        # -------------------------
        # ID Columns by name
        # -------------------------
        if any(word in col for word in ID_KEYWORDS):
            ids.append(column)
            continue

        # -------------------------
        # Numeric Measures
        # -------------------------
        if pd.api.types.is_numeric_dtype(df[column]):

            unique_ratio = df[column].nunique(dropna=True) / max(len(df), 1)

            # If almost every value is unique,
            # it is probably an ID column.
            if unique_ratio > 0.95:
                ids.append(column)
            else:
                measures.append(column)

            continue

        # -------------------------
        # Geography
        # -------------------------
        if any(word in col for word in GEO_KEYWORDS):
            geo.append(column)
            dimensions.append(column)
            continue

        # -------------------------
        # Default Dimension
        # -------------------------
        dimensions.append(column)

    return {
        "dimensions": dimensions,
        "measures": measures,
        "dates": dates,
        "ids": ids,
        "geo": geo,
        "booleans": booleans,
    }