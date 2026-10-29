from flask import Flask, jsonify, request

app = Flask (__name__)

id = 0
filme_bd = []

@app.route("/filmes")
def retornarFilme():
    return jsonify (filme_bd)  

@app.route("/filmes", methods=["POST"])
def salvarFilme():
    global id
    id = id + 1
    dados = request.get_json()
    nome = dados.get("nome")
    ano = dados.get("ano")
    diretor = dados.get ("diretor")
    filme = {"id" : id, "nome" : nome, "ano" : ano, "diretor" : diretor } 
    filme_bd.append(filme)
    return jsonify(filme)

@app.route("/filmes/<int:id>", methods = ["PUT"])
def alterarFilme(id) :
    dados = request.get_json()
    for filme in filme_bd:
        if filme["id"] == id:
            filme["nome"] = dados.get("nome")
            filme["ano"] = int(dados.get("ano"))
            filme["diretor"] =dados.get("diretor")
            return jsonify(filme), 200
    return jsonify({"erro": "filme nao encontrada"}), 404

@app.route("/filme/<int:id>",methods = ["DELETE"])
def remover_filme(id):
    for filme in filme_bd:
        if filme["id"] == id:
            filme_bd.remove(filme)
            return "", 204
    
    return jsonify({"erro": "filme nao encontrada"}), 404
  

app.run(debug=True) 