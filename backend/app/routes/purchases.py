from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter(prefix="/purchases", tags=["Purchases"])

@router.post("/", response_model=schemas.Purchase)
def create_purchase(purchase: schemas.PurchaseCreate, db: Session = Depends(database.get_db)):
    db_purchase = models.Purchase(**purchase.dict())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return db_purchase

@router.get("/", response_model=list[schemas.Purchase])
def read_purchases(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return db.query(models.Purchase).offset(skip).limit(limit).all()
