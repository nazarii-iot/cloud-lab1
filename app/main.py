import os
from contextlib import asynccontextmanager

import psycopg
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://clouduser:cloudpass@localhost:5432/clouddb",
)


def initialize_database():
    with psycopg.connect(DATABASE_URL, connect_timeout=5) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)


@asynccontextmanager
async def lifespan(app: FastAPI):
    if os.getenv("DATABASE_URL"):
        initialize_database()
    yield


app = FastAPI(
    title="Cloud Lab 1 REST API",
    description="REST API with PostgreSQL database",
    version="1.0.0",
    lifespan=lifespan,
)


class ItemCreate(BaseModel):
    name: str


@app.get("/")
def root():
    return {"message": "Cloud Lab 1 API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    try:
        with psycopg.connect(DATABASE_URL, connect_timeout=5) as connection:
            rows = connection.execute(
                "SELECT id, name FROM items ORDER BY id"
            ).fetchall()
            return [{"id": row[0], "name": row[1]} for row in rows]
    except psycopg.Error:
        raise HTTPException(status_code=503, detail="Database unavailable")


@app.post("/items", status_code=201)
def create_item(item: ItemCreate):
    try:
        with psycopg.connect(DATABASE_URL, connect_timeout=5) as connection:
            row = connection.execute(
                "INSERT INTO items (name) VALUES (%s) RETURNING id, name",
                (item.name,),
            ).fetchone()
            return {"id": row[0], "name": row[1]}
    except psycopg.Error:
        raise HTTPException(status_code=503, detail="Database unavailable")
