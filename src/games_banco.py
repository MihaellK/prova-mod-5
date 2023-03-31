from sqlalchemy.orm import Session, sessionmaker
from models.game import GamesInfo

session = Session()

dsr = GamesInfo(nome="DEAD SPACE REMAKE", plat="PS5", preco=350.00, quant="10")
di2 = GamesInfo(nome="DEAD ISLAND 2", plat="PC", preco=299.00, quant="10")
hl = GamesInfo(nome="HOGWARTS LEGACY", plat="PC", preco=219.00, quant="7")
wh = GamesInfo(nome="WILD HEARTS", plat="XBOX", preco=350.00, quant="7")
re4 = GamesInfo(nome="RESIDENT EVIL 4", plat="PS5", preco=289.00,
                       quant="10")
link = GamesInfo(nome="THE LEGEND OF ZELDA: TEARS OF THE KINGDOM",
                  plat="SWITCH", preco=299.00, quant="10")
fsp = GamesInfo(nome="FORSPOKEN", plat="PC", preco=299.00, quant="8")
session.add(dsr, di2, hl, wh, re4, link, fsp)
session.commit()

