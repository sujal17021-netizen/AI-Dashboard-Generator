import hashlib
import json
import pandas as pd


def generate_dataset_hash(df: pd.DataFrame) -> str:
    """
    Generate a stable SHA256 hash from dataset contents.
    """

    # Replace NaN values
    df = df.where(pd.notnull(df), None)

    # Convert datetime columns to strings
    for column in df.columns:

        if pd.api.types.is_datetime64_any_dtype(df[column]):

            df[column] = df[column].astype(str)

    # Sort columns
    df = df.reindex(sorted(df.columns), axis=1)

    # Convert to records
    records = df.to_dict(orient="records")

    # Sort rows
    records = sorted(
        records,
        key=lambda row: json.dumps(
            row,
            sort_keys=True,
            default=str
        )
    )

    json_string = json.dumps(
        records,
        sort_keys=True,
        separators=(",", ":"),
        default=str
    )

    return hashlib.sha256(
        json_string.encode("utf-8")
    ).hexdigest()