from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from .tracking_dimension import TrackingDimension


class ProductGroup(Base):
    __tablename__ = "product_groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    tracking_dimension_id = Column(Integer, ForeignKey("tracking_dimensions.id"))

    tracking_dimension = relationship("TrackingDimension")
