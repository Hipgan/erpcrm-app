# schemas/purchase.py
from pydantic import BaseModel
from datetime import datetime

class PurchaseBase(BaseModel):
    customer_id: int
    product_id: int

class PurchaseCreate(PurchaseBase):
    pass

class Purchase(PurchaseBase):
    id: int
    purchase_date: datetime

    class Config:
        from_attributes = True