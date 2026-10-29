from flask import Flask, request, jsonify

app = Flask(__name__)

id_contador = 0 
carros_bd = []

@app.route("/carros")
def retornarCarros():
    return jsonify(carros_bd), 200

@app.route("/carros", methods=["POST"])
def salvarCarro():
    global id_contador 
    id_contador += 1 
    dados = request.get_json()
    carro = {
        "id": id_contador, 
        "modelo": dados.get("modelo"), 
        "marca": dados.get("marca"), 
        "ano": dados.get("ano")
    }
    carros_bd.append(carro)
    return jsonify(carro), 201

@app.route("/carros/<int:id>", methods=["PUT"])
def editarCarro(id):
    dados = request.get_json()
    for carro in carros_bd:
        if carro["id"] == id:
            carro["modelo"] = dados.get("modelo")
            carro["marca"] = dados.get("marca")
            carro["ano"] = dados.get("ano")
            return jsonify(carro), 200
    return jsonify({"erro": "Carro nao encontrado"}), 404

@app.route("/carros/<int:id>", methods=["DELETE"])
def removerCarro(id):
    for carro in carros_bd:
        if carro["id"] == id:
            carros_bd.remove(carro)
            return "", 204
    return jsonify({"erro": "Carro nao encontrado"}), 404

app.run(debug=True)