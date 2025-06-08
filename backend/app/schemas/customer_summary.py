# backend/app/schemas/summary.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CustomerSummary(BaseModel):
    customer_id: int
    name: str
    total_contracts: int
    total_purchases: float
    total_paid: float
    total_due: float
    last_payment_date: Optional[datetime]

    class Config:
        from_attributes = True
