#import todas as libs
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.base import Base
from model.game import Game
from flask import Flask, render_template,request,redirect

#instancia o app do flask
app = Flask(__name__)

#nome do banco de dados e o tipo
engine = create_engine('sqlite:///database.db', echo=True) 

#instancia a sessão
Session = sessionmaker(bind=engine)

#cria uma variavel para a sessão
session = Session()

#cria o arquivo do banco de dados
Base.metadata.create_all(engine)

#rota da pagina inicial listando os games
@app.route("/")
def index():
    #puxa do banco de dados todos os games cadastrados
    games = session.query(Game).all()
    #verifica se a lista de games está vazia
    if games is None:
        games = []
    #retorna a pagina index.html com a lista de games
    return render_template("index.html", games=games)

#rota para adicionar um game
@app.route("/add", methods=["POST"])
def add_game():
    #pega as informações correspondentes do formulario
    nome= request.form["nome"]
    plataforma= request.form["plataforma"]
    preco= request.form["preco"]
    quantidade= request.form["quantidade"]
     
    #verifica se alguma informação veio vazia
    if nome is not None and plataforma is not None and preco is not None and quantidade is not None:
        game = Game(
        nome= nome,
        plataforma= plataforma,
        preco= preco,
        quantidade= quantidade)
        session.add(game)
        session.commit()    
        return redirect("/")
    else:
        return redirect("/")

#cria o servidor
app.run(host='0.0.0.0', port=3000, debug=True)

