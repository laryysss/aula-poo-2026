from flask import Flask, request, jsonify

app = Flask(__name__)

id_contador = 0 
restaurantes_bd = []

@app.route("/restaurantes")
def retornarRestaurantes():
    return jsonify(restaurantes_bd), 200

@app.route("/restaurantes", methods=["POST"])
def salvarRestaurante():
    global id_contador 
    id_contador += 1 
    dados = request.get_json()
    restaurante = {
        "id": id_contador, 
        "nome": dados.get("nome"), 
        "tipo": dados.get("tipo"), 
        "cidade": dados.get("cidade")
    }
    restaurantes_bd.append(restaurante)
    return jsonify(restaurante), 201

@app.route("/restaurantes/<int:id>", methods=["PUT"])
def editarRestaurante(id):
    dados = request.get_json()
    for restaurante in restaurantes_bd:
        if restaurante["id"] == id:
            restaurante["nome"] = dados.get("nome")
            restaurante["tipo"] = dados.get("tipo")
            restaurante["cidade"] = dados.get("cidade")
            return jsonify(restaurante), 200
    return jsonify({"erro": "Restaurante nao encontrado"}), 404

@app.route("/restaurantes/<int:id>", methods=["DELETE"])
def removerRestaurante(id):
    for restaurante in restaurantes_bd:
        if restaurante["id"] == id:
            restaurantes_bd.remove(restaurante)
            return "", 204
    return jsonify({"erro": "Restaurante nao encontrado"}), 404


app.run(debug=True)