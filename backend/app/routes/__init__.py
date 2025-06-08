from .products import router as products_router
from .customers import router as customers_router
from .payments import router as payments_router
from .contracts import router as contracts_router
from .purchases import router as purchases_router
from .customer_summary import router as customer_summary_router


from fastapi import APIRouter

router = APIRouter()
router.include_router(products_router)#, prefix="/products", tags=["products"])
router.include_router(customers_router)#, prefix="/customers", tags=["customers"])
router.include_router(payments_router)#, prefix="/payments", tags=["payments"])
router.include_router(contracts_router)#, prefix="/contracts", tags=["contracts"])
router.include_router(purchases_router)#, prefix="/purchases", tags=["purchases"])  # ✅ correct! 
router.include_router(customer_summary_router)
