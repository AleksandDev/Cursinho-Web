from sqlalchemy import Column, Integer, String, Text

if __name__ != '__main__':
    from .bd import Base
else:
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()

class Curso(Base):
    __tablename__ = 'cursos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=False)
    duracao = Column(String(50), nullable=False)

    def __init__(self, nome, descricao, duracao):
        self.nome = nome
        self.descricao = descricao
        self.duracao = duracao

    def get_nome(self):
        return self.nome

    def get_descricao(self):
        return self.descricao

    def get_duracao(self):
        return self.duracao