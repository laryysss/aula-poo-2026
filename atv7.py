from flask import Flask, request, jsonify

app = Flask(__name__)

id_contador = 0 
cidades_bd = []

@app.route("/cidades")
def retornarCidades():
    return jsonify(cidades_bd), 200

@app.route("/cidades", methods=["POST"])
def salvarCidade():
    global id_contador 
    id_contador += 1 
    dados = request.get_json()
    cidade = {
        "id": id_contador, 
        "nome": dados.get("nome"), 
        "estado": dados.get("estado"), 
        "populacao": dados.get("populacao")
    }
    cidades_bd.append(cidade)
    return jsonify(cidade), 201

@app.route("/cidades/<int:id>", methods=["PUT"])
def editarCidade(id):
    dados = request.get_json()
    for cidade in cidades_bd:
        if cidade["id"] == id:
            cidade["nome"] = dados.get("nome")
            cidade["estado"] = dados.get("estado")
            cidade["populacao"] = dados.get("populacao")
            return jsonify(cidade), 200
    return jsonify({"erro": "Cidade nao encontrada"}), 404

@app.route("/cidades/<int:id>", methods=["DELETE"])
def removerCidade(id):
    for cidade in cidades_bd:
        if cidade["id"] == id:
            cidades_bd.remove(cidade)
            return "", 204
    return jsonify({"erro": "Cidade nao encontrada"}), 404

app.run(debug=True)