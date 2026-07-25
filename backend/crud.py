from sqlalchemy.orm import Session
from models import UploadedFile, Dataset, DatasetRow

import pandas as pd
import numpy as np

from datetime import datetime, date, time


# ==========================================================
# Fetch Dataset
# ==========================================================
import pandas as pd
from sqlalchemy.orm import Session
from models import DatasetRow


def fetch_dataset(
    db: Session,
    dataset_id: int
):

    print("Fetching dataset...")

    rows = (
        db.query(DatasetRow)
        .filter(DatasetRow.dataset_id == dataset_id)
        .limit(10000)      # <-- TEMPORARY
        .all()
    )

    print("Rows fetched :", len(rows))

    dataframe = pd.DataFrame(
        [row.row_data for row in rows]
    )

    print("DataFrame created")

    return dataframe


# ==========================================================
# Save Uploaded File (Old)
# ==========================================================
def save_uploaded_file(
    db: Session,
    filename: str,
    rows: int,
    columns: int,
    file_url: str = ""
):

    new_file = UploadedFile(
        filename=filename,
        rows=rows,
        columns=columns,
        file_url=file_url
    )

    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return new_file


# ==========================================================
# Save Dataset
# ==========================================================
def save_dataset(
    db: Session,
    filename: str,
    dataset_hash: str
):

    dataset = Dataset(
        filename=filename,
        dataset_hash=dataset_hash
    )

    db.add(dataset)
    db.commit()
    db.refresh(dataset)

    return dataset


# ==========================================================
# Find Dataset By Hash
# ==========================================================
def get_dataset_by_hash(
    db: Session,
    dataset_hash: str
):

    print("=" * 60)
    print("Searching Hash :", dataset_hash)

    dataset = (
        db.query(Dataset)
        .filter(Dataset.dataset_hash == dataset_hash)
        .first()
    )

    print("Database Result :", dataset)
    print("=" * 60)

    return dataset


# ==========================================================
# Convert Values
# ==========================================================
def convert_value(value):

    if pd.isna(value):
        return None

    if isinstance(value, (pd.Timestamp, datetime, date)):
        return value.isoformat()

    if isinstance(value, time):
        return value.isoformat()

    if isinstance(value, np.integer):
        return int(value)

    if isinstance(value, np.floating):
        return float(value)

    if isinstance(value, np.bool_):
        return bool(value)

    return value


# ==========================================================
# Save Dataset Rows
# ==========================================================
def save_dataset_rows(
    db: Session,
    dataset_id: int,
    dataframe: pd.DataFrame,
    batch_size: int = 5000
):

    print("========== SAVING ROWS ==========")

    total_rows = len(dataframe)

    for start in range(0, total_rows, batch_size):

        end = min(start + batch_size, total_rows)

        batch = []

        for _, row in dataframe.iloc[start:end].iterrows():

            row_dict = {
                column: convert_value(value)
                for column, value in row.items()
            }

            batch.append(
                DatasetRow(
                    dataset_id=dataset_id,
                    row_data=row_dict
                )
            )

        db.bulk_save_objects(batch)
        db.commit()

        print(f"Inserted {end}/{total_rows}")

    print("All rows inserted successfully.")