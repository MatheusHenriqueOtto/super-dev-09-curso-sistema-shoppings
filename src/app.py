import sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.controllers import avaliacoes_controllers, clientes_controllers, contratos_controllers
from src.controllers import estacionamento_controllers, funcionarios_controllers, lojas_controllers
from src.controllers import shoppings_controllers



app = FastAPI(
    title="Mallverse API",
    description="API para gerenciamento de shoppings",
    version="1.0.0"
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
app.include_router(clientes_controllers.router)
app.include_router(avaliacoes_controllers.router)
app.include_router(contratos_controllers.router)
app.include_router(lojas_controllers.router)
app.include_router(funcionarios_controllers.router)
app.include_router(estacionamento_controllers.router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
    "src.app:app",
    host="127.0.0.1",
    port=8000,
    reload=True,
)
