from fastapi import FastAPI
from app.database import Base, engine
from app.routes.products import router as products_router
from app.routes.customers import router as customer_router
from app.routes.contracts import router as contracts_router
from app.routes.payments import router as payments_router
from app.routes.purchases import router as purchases_router
from app.routes.customer_summary import router as customer_summary_router
from app.routes.tracking_dimensions import router as tracking_router
from app.routes.product_groups import router as product_group_router

app = FastAPI()

# Alembic? → laat dit weg. Geen alembic? → tijdelijk oké:
# Base.metadata.create_all(bind=engine)

# Routers activeren
app.include_router(products_router)
app.include_router(customer_router)
app.include_router(contracts_router)
app.include_router(payments_router)
app.include_router(purchases_router)
app.include_router(customer_summary_router)
app.include_router(tracking_router)
app.include_router(product_group_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
