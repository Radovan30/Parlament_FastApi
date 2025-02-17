from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.admin_endpoints import router as admin_router
from app.api.public_endpoints import router as public_router
from app.models import Foods
from db.database import SessionLocal

import shutil
import os

app = FastAPI(title="FastAPI Restaurant API")

UPLOAD_DIR = "app/static/uploads/foods"

app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(public_router, prefix="/public", tags=["Public"])

app.mount("/static", StaticFiles(directory="app/static"), name="static")

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


@app.post("/upload_food_image/")
async def upload_food_image(food_id: int, file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[-1]
    if file_ext.lower() not in [".jpg", ".jpeg", ".png", ".webp"]:
        raise HTTPException(status_code=400, detail="Nepodporovaný formát obrázku.")

    file_name = f"food_{food_id}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, file_name)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    image_url = f"/app/static/uploads/foods/{file_name}"

    # Aktualizace databáze s cestou k obrázku
    db = SessionLocal()
    try:
        food = db.query(Foods).filter(Foods.id == food_id).first()
        if not food:
            raise HTTPException(status_code=404, detail="Jídlo s tímto ID neexistuje.")

        food.image_url = image_url
        db.commit()
    finally:
        db.close()  # Zavření databázového spojení

    return {"message": "Obrázek byl úspěšně nahrán", "image_url": image_url}