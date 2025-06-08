from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Contract(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    total_amount = Column(Float, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    number_of_installments = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    payments = relationship("Payment", back_populates="contract")
    customer = relationship("Customer", back_populates="contracts")
