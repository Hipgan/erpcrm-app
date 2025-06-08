# schemas/payment.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PaymentBase(BaseModel):
    amount: float
    status: Optional[str] = "open"
    due_date: Optional[datetime] = None

class PaymentCreate(PaymentBase):
    customer_id: int

class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = None

class PaymentOut(PaymentBase):
    id: int
    customer_id: int
    created_at: datetime

    class Config:
        from_attributes = True
