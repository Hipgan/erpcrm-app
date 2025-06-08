# schemas/contract.py
from pydantic import BaseModel
from datetime import date

class ContractBase(BaseModel):
    customer_id: int
    total_amount: float
    start_date: date
    end_date: date
    num_installments: int

class ContractCreate(ContractBase):
    pass

class Contract(ContractBase):
    id: int

    class Config:
        from_attributes = True