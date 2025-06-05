from fastapi import FastAPI
from src.infra.sqlalchemy.config.database import criar_db
from src.routers.series_router import router as series_router


criar_db()


app = FastAPI()
app.include_router(series_router)
