from fastapi import APIRouter
from .schemas import Customer

router = APIRouter()

@router.get("/ping")
def ping():
    return {"message": "pong"}

@router.post("/customers")
def create_customer(customer: Customer):
    return {"message": f"Customer {customer.name} created"}
