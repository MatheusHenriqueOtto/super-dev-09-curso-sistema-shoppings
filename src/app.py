
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from fastapi import FastAPI
import sys


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.controllers import shoppings_controllers

app = FastAPI(
    title="Mallverse API",
    description="Projeto par gerenciamento de shoppings",
    version="0.1.0",
)

origins = [
    "http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(shoppings_controllers.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.app:app", host="127.0.0.1", port=8000, reload=True)

