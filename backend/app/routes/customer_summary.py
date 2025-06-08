from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from datetime import datetime
from app.schemas.customer_summary import CustomerSummary


router = APIRouter(
    prefix="",
    tags=["Summary"]
)
@router.get("/customers/{customer_id}/summary", response_model=CustomerSummary)
def get_customer_summary(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    total_contracts = db.query(models.Contract).filter(models.Contract.customer_id == customer_id).count()
    total_purchases = sum([p.product.price for p in customer.purchases])
    total_paid = sum([p.amount for p in customer.payments])
    total_due = total_purchases - total_paid

    last_payment = (
        db.query(models.Payment)
        .filter(models.Payment.customer_id == customer_id)
        .order_by(models.Payment.created_at.desc())  # 🔄 hier aangepast
        .first()
    )
    last_payment_date = last_payment.created_at if last_payment else None

    return {
        "customer_id": customer.id,
        "name": customer.name,
        "total_contracts": total_contracts,
        "total_purchases": total_purchases,
        "total_paid": total_paid,
        "total_due": total_due,
        "last_payment_date": last_payment_date,
    }
