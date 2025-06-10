from fastapi import FastAPI
from app.routes import usuarios, libros
import logging
from dotenv import load_dotenv
import os

load_dotenv()

# Logging config
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)
logger.info("Servidor iniciado")

app = FastAPI(title="Biblioteca Colectiva")

app.include_router(usuarios.router)
app.include_router(libros.router)
