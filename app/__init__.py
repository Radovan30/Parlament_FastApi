from fastapi import FastAPI
from app.api.admin_endpoints import router as admin_router
from app.api.public_endpoints import router as public_router
from config import SECRET_KEY

def create_app():
    """ Inicializace FastAPI aplikace """
    app = FastAPI(
        title="FastAPI Restaurant",
        description="REST API for a restaurant application",
        version="1.0.0",
    )

    # Nastavení configu (např. SECRET_KEY, pokud ho aplikace potřebuje)
    app.state.SECRET_KEY = SECRET_KEY

    # Registrace routerů (FastAPI místo Flask Blueprintů používá `include_router`)
    app.include_router(public_router, prefix="/api/public", tags=["Public"])
    app.include_router(admin_router, prefix="/api/admin", tags=["Admin"])

    return app

