from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models, database

router = APIRouter(prefix="/payments", tags=["Payments"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.PaymentOut)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    db_payment = models.Payment(**payment.dict())
    db.add(db_payment)
    db.commit()

    # Update total_due van de klant
    customer = db.query(models.Customer).filter(models.Customer.id == payment.customer_id).first()
    if customer:
        customer.total_due += payment.amount
        db.commit()
        db.refresh(customer)

    db.refresh(db_payment)
    return db_payment

@router.get("/", response_model=list[schemas.PaymentOut])
def get_all_payments(db: Session = Depends(get_db)):
    return db.query(models.Payment).all()

@router.get("/customer/{customer_id}", response_model=list[schemas.PaymentOut])
def get_payments_by_customer(customer_id: int, db: Session = Depends(get_db)):
    return db.query(models.Payment).filter(models.Payment.customer_id == customer_id).all()

@router.put("/{payment_id}", response_model=schemas.PaymentOut)
def update_payment(payment_id: int, update: schemas.PaymentUpdate, db: Session = Depends(get_db)):
    payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    
    for key, value in update.dict(exclude_unset=True).items():
        setattr(payment, key, value)
    db.commit()
    db.refresh(payment)
    return payment

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    # Verminder total_due van customer
    customer = payment.customer
    if customer:
        customer.total_due -= payment.amount
        db.commit()

    db.delete(payment)
    db.commit()
    return {"message": f"Payment {payment_id} verwijderd"}
