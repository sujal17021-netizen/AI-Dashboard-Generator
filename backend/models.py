
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class UploadedFile(Base):

    __tablename__ = "uploaded_files"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    rows = Column(Integer)

    columns = Column(Integer)

    file_url = Column(String)
class Dataset(Base):

    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    dataset_hash = Column(String, unique=True, index=True)

    uploaded_at = Column(DateTime, default=datetime.utcnow)

    rows = relationship(
        "DatasetRow",
        back_populates="dataset",
        cascade="all, delete"
    )


class DatasetRow(Base):

    __tablename__ = "dataset_rows"

    id = Column(Integer, primary_key=True, index=True)

    dataset_id = Column(
        Integer,
        ForeignKey("datasets.id")
    )

    row_data = Column(JSONB)

    dataset = relationship(
        "Dataset",
        back_populates="rows"
    )