from app.schemas.product import ProductOut
from app.schemas.contract import Contract, ContractCreate

from fastapi import APIRouter, Depends, HTTPException
from app import models
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db

router = APIRouter(
    prefix="/contracts",
    tags=["Contracts"]
)

# Voorbeeldroute
@router.post("/", response_model=Contract)
def create_contract(contract: ContractCreate, db: Session = Depends(get_db)):
    db_contract = models.contract.Contract(**contract.dict())
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract

@router.get("/", response_model=list[Contract])
def get_contracts(db: Session = Depends(get_db)):
    return db.query(models.Contract).all()