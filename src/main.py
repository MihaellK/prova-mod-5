from flask import Flask, render_template, jsonify, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.game import GamesInfo

engine = create_engine('sqlite:///games.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)



app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template("index.html", infos = getInfo())

# @app.route('/login',methods = ['POST', 'GET'])
@app.route('/postGames', methods = ['POST', 'GET'])
def addGames():
    # populando a tabela

    dsr = GamesInfo(nome="DEAD SPACE REMAKE", plat="PS5", preco=350.00, quant="10")
    di2 = GamesInfo(nome="DEAD ISLAND 2", plat="PC", preco=299.00, quant="10")
    hl = GamesInfo(nome="HOGWARTS LEGACY", plat="PC", preco=219.00, quant="7")
    wh = GamesInfo(nome="WILD HEARTS", plat="XBOX", preco=350.00, quant="7")
    re4 = GamesInfo(nome="RESIDENT EVIL 4", plat="PS5", preco=289.00,
                        quant="10")
    link = GamesInfo(nome="THE LEGEND OF ZELDA: TEARS OF THE KINGDOM",
                    plat="SWITCH", preco=299.00, quant="10")
    fsp = GamesInfo(nome="FORSPOKEN", plat="PC", preco=299.00, quant="8")
    session.add(dsr)
    session.add(di2)
    session.add(hl)
    session.add(wh)
    session.add(re4)
    session.add(link)
    session.add(fsp)
    session.commit()
    return redirect('/')
# 

@app.route("/getGames", methods=['GET', 'POST'])
def getInfo():
    try:
        # Abre sessão e faz um query ao banco
        get_session = Session()
        info = get_session.query(GamesInfo).order_by(GamesInfo.id)
        print(info)
        # retorna a informação em json
        return jsonify(info.info_as_json())
    except Exception as err:
        print(str(err))

if __name__ == "__main__":
    app.run(host="localhost", port=3000)