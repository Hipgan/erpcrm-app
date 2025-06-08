from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.product_group import ProductGroupCreate, ProductGroupOut
from app.models.product_group import ProductGroup
from app.database import get_db

router = APIRouter(prefix="/product-groups", tags=["Product Groups"])

@router.post("/", response_model=ProductGroupOut)
def create_product_group(data: ProductGroupCreate, db: Session = Depends(get_db)):
    pg = ProductGroup(name=data.name, tracking_dimension_id=data.tracking_dimension_id)
    db.add(pg)
    db.commit()
    db.refresh(pg)
    return pg

@router.get("/", response_model=List[ProductGroupOut])
def list_product_groups(db: Session = Depends(get_db)):
    return db.query(ProductGroup).all()
