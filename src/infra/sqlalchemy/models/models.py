from infra.sqlalchemy.config.database import Base
from sqlalchemy import Column, Integer, String

class Serie(Base):
    __tablename__ = 'serie'

    id = Column(Integer, primary_key=True, Index=True)
    titulo = Column(String)
    ano = Column(Integer)
    genero = Column(String)
    qtd_temporadas =Column(Integer)