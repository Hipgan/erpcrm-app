from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.tracking_dimension import TrackingDimensionCreate, TrackingDimensionOut
from app.models.tracking_dimension import TrackingDimension
from app.database import get_db

router = APIRouter(prefix="/tracking-dimensions", tags=["Tracking Dimensions"])

@router.post("/", response_model=TrackingDimensionOut)
def create_tracking_dimension(data: TrackingDimensionCreate, db: Session = Depends(get_db)):
    td = TrackingDimension(name=data.name, is_active=data.is_active)
    db.add(td)
    db.commit()
    db.refresh(td)
    return td

@router.get("/", response_model=List[TrackingDimensionOut])
def list_tracking_dimensions(db: Session = Depends(get_db)):
    return db.query(TrackingDimension).all()
