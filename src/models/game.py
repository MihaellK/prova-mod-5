from models.base import Base
from sqlalchemy import Integer, Float, Column, String

class GamesInfo(Base):
    __tablename__ = "games_info"

    # Nome do Jogo, Plataforma, Preço e Quantidade

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    plat = Column(String)
    preco = Column(Float)
    quant = Column(Integer)

    def info_as_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "plat": self.plat,
            "preco": self.preco,
            "quant": self.quant
        }

    def __repr__(self) -> str:
        return f"id = {self.id}"