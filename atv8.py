from flask import Flask, request, jsonify

app = Flask(__name__)

id_contador = 0 
jogos_bd = []

@app.route("/jogos")
def retornarJogos():
    return jsonify(jogos_bd), 200

@app.route("/jogos", methods=["POST"])
def salvarJogo():
    global id_contador 
    id_contador += 1 
    dados = request.get_json()
    jogo = {
        "id": id_contador, 
        "nome": dados.get("nome"), 
        "genero": dados.get("genero"), 
        "ano": dados.get("ano")
    }
    jogos_bd.append(jogo)
    return jsonify(jogo), 201

@app.route("/jogos/<int:id>", methods=["PUT"])
def editarJogo(id):
    dados = request.get_json()
    for jogo in jogos_bd:
        if jogo["id"] == id:
            jogo["nome"] = dados.get("nome")
            jogo["genero"] = dados.get("genero")
            jogo["ano"] = dados.get("ano")
            return jsonify(jogo), 200
    return jsonify({"erro": "Jogo nao encontrado"}), 404

@app.route("/jogos/<int:id>", methods=["DELETE"])
def removerJogo(id):
    for jogo in jogos_bd:
        if jogo["id"] == id:
            jogos_bd.remove(jogo)
            return "", 204
    return jsonify({"erro": "Jogo nao encontrado"}), 404
app.run(debug=True)