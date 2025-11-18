from fastapi import FastAPI, Response
from app.routers import properties, ptam
from app.db import Base, engine

app = FastAPI(title="Plataforma Imobiliária API (FastAPI)")

# cria tabelas para ambiente de dev
Base.metadata.create_all(bind=engine)

app.include_router(properties.router, prefix="/api/properties", tags=["properties"])
app.include_router(ptam.router, prefix="/api/ptam", tags=["ptam"])

@app.get("/")
def root():
    return {"ok": True}
