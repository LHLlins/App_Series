from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.repositorios.series import RepositorioSerie
from src.infra.sqlalchemy.config.database import get_db

router = APIRouter(prefix="/series", tags=["series"])

@router.post('/')
def criar_serie(serie: schemas.Serie, db: Session = Depends(get_db)):
    serie_criada = RepositorioSerie(db).criar(serie)
    return serie_criada

@router.get('/')
def listar_serie(db: Session = Depends(get_db)):
    return RepositorioSerie(db).listar()

@router.get('/{series_id}')
def obter_serie(serie_id: int, db: Session = Depends(get_db)):
    serie = RepositorioSerie(db).obter(serie_id)
    return serie

@router.delete('/{series_id}')
def remover_serie(serie_id: int, db: Session = Depends(get_db)):
    RepositorioSerie(db).remover(serie_id)
    return {'Removido com sucesso!'}
