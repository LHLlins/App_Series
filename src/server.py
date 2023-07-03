from fastapi import FastAPI, Depends
from src.infra.sqlalchemy.config.database import criar_db, get_db
from . import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.series import RepositorioSerie



criar_db()


app = FastAPI()

@app.pos('/series')
def criar_serie(serie: schemas.Serie, db: Session = Depends(get_db)):
    serie_criada = RepositorioSerie(db).criar(serie)
    return serie_criada,

@app.get('/series')
def listar_serie(db: Session = Depends(get_db)):
    return RepositorioSerie(db).listar()

@app.get('/series/{series_id}')
def obter_serie(serie_id: int, db: Session = Depends(get_db)):
    serie = RepositorioSerie(db).obter(serie_id)
    return serie


@app.delete('/series/{series_id}')
def remover_serie(serie_id: int, db: Session = Depends(get_db)):
    RepositorioSerie(db).remover(serie_id)
    return {'Removido com sucesso!'}
