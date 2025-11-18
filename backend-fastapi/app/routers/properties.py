from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.property import Property

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("")
def list_properties(db: Session = Depends(get_db)):
    return db.query(Property).limit(50).all()

@router.post("")
def create_property(payload: dict, db: Session = Depends(get_db)):
    p = Property(**payload)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p
