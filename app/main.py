from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.enums import Estado
from app.schemas import ZonaCreate, PatineteCreate

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/zonas/", response_model=schemas.ZonaOut)
def crear_zona(zona: ZonaCreate, db: Session = Depends(get_db)):
    nueva = models.Zona(**zona.model_dump())
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


@app.post("/patinetes/", response_model=schemas.PatineteOut)
def crear_patinete(p: PatineteCreate, db: Session = Depends(get_db)):
    patinete = models.Patinete(**p.model_dump(), estado=Estado.disponible)
    db.add(patinete)
    db.commit()
    db.refresh(patinete)
    return patinete


@app.post("/zonas/{zona_id}/mantenimiento", response_model=list[schemas.PatineteOut])
def mantenimiento(zona_id: int, db: Session = Depends(get_db)):
    patinetes = db.query(models.Patinete).filter(
        models.Patinete.zona_id == zona_id,
        models.Patinete.bateria < 15).all()

    for p in patinetes:
        p.estado = Estado.mantenimiento

    db.commit()
    return patinetes