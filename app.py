from flask import Flask, render_template

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/usuarios")
def usuario():
    usuario = [1, "Jackson Gomes", "Professor"]
    aluno = ["André Guedes", "Lucas Santos", "Alícia Duarte", "Raiane Caroline"]
    return render_template("index.html", usuario=usuario, aluno=aluno)

@app.route("/contatos")
def contato():
    nomeAula = "Aula Python para Web"
    return render_template("index.html", nome=nomeAula)