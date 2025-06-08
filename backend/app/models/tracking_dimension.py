from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base  # of van waar jij Base importeert

class TrackingDimension(Base):
    __tablename__ = "tracking_dimensions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
