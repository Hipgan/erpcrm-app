from pydantic import BaseModel
from typing import Optional

class TrackingDimensionBase(BaseModel):
    name: str
    is_active: Optional[bool] = True

class TrackingDimensionCreate(TrackingDimensionBase):
    pass

class TrackingDimensionOut(TrackingDimensionBase):
    id: int

    class Config:
        from_attributes = True  # Pydantic v2
