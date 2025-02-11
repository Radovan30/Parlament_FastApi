from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from app.api.admin_endpoints import router as admin_router
from app.api.public_endpoints import router as public_router

app = FastAPI(title="FastAPI Restaurant API")

app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(public_router, prefix="/public", tags=["Public"])

# Nastavení CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Restaurant API"}

# Přesměrování favicon, aby se eliminovala 404 chyba
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204)