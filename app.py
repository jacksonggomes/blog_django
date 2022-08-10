from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/contato")
def contatos():
    return """<html>
            <head>
                <title> Contatos </title>
            </head>
            <body>
                <h1>Jackson Gonçalves Gomes<h1>
                <h2>jackson.am2009@gmail.com<h2>
            </body>
        </html>"""