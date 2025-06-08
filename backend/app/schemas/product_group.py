from pydantic import BaseModel
from typing import Optional

class ProductGroupBase(BaseModel):
    name: str
    tracking_dimension_id: int  # Verwijzing naar een tracking dimension

class ProductGroupCreate(ProductGroupBase):
    pass

class ProductGroupOut(ProductGroupBase):
    id: int

    class Config:
        from_attributes = True  # Voor Pydantic v2 (zoals jij gebruikt)
