from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.api.routes.products import router as products_router
from app.api.routes.analysis import router as analysis_router
from app.db.init_db import init_db

app = FastAPI(
    title="AI选品 + 利润测算 Agent",
    version="1.0.0",
    description="Amazon 跨境电商选品分析与利润测算系统"
)

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(health_router, tags=["Health"])
app.include_router(products_router, prefix="/products", tags=["Products"])
app.include_router(analysis_router, prefix="/analysis", tags=["Analysis"])


@app.get("/")
def root():
    return {
        "message": "AI选品 + 利润测算 Agent is running",
        "docs": "/docs"
    }
