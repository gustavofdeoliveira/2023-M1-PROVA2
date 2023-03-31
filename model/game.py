#imports do sqlalchemy e da classe Base
from sqlalchemy import Column, Integer, String, Float
from model.base import Base

#instacia a clase Game
class Game(Base):
    #nome da tabela
    __tablename__ = 'games'
    #atributos da tabela games
    id = Column(Integer, primary_key=True, autoincrement='auto')
    nome = Column(String)
    plataforma = Column(String)
    preco = Column(Float)
    quantidade = Column(Integer)

    def __repr__(self):
        return f'Games {self}'