from flask import Flask, request, jsonify

app = Flask(__name__)

id_contador = 0 
musicas_bd = []

@app.route("/musicas")
def retornarMusicas():
    return jsonify(musicas_bd), 200

@app.route("/musicas", methods=["POST"])
def salvarMusica():
    global id_contador 
    id_contador += 1 
    dados = request.get_json()
    musica = {
        "id": id_contador, 
        "nome": dados.get("nome"), 
        "artista": dados.get("artista"), 
        "ano": dados.get("ano")
    }
    musicas_bd.append(musica)
    return jsonify(musica), 201

@app.route("/musicas/<int:id>", methods=["PUT"])
def editarMusica(id):
    dados = request.get_json()
    for musica in musicas_bd:
        if musica["id"] == id:
            musica["nome"] = dados.get("nome")
            musica["artista"] = dados.get("artista")
            musica["ano"] = dados.get("ano")
            return jsonify(musica), 200
    return jsonify({"erro": "Musica nao encontrada"}), 404

@app.route("/musicas/<int:id>", methods=["DELETE"])
def removerMusica(id):
    for musica in musicas_bd:
        if musica["id"] == id:
            musicas_bd.remove(musica)
            return "", 204
    return jsonify({"erro": "Musica nao encontrada"}), 404

app.run(debug=True)