from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/contato")
def contatos():
    return "Jackson Gonçalves Gomes"