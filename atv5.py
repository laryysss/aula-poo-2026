from flask import Flask, request, jsonify

app = Flask(__name__)

id_contador = 0 
produtos_bd = []

@app.route("/produtos")
def retornarProdutos():
    return jsonify(produtos_bd), 200

@app.route("/produtos", methods=["POST"])
def salvarProduto():
    global id_contador 
    id_contador += 1 
    dados = request.get_json()
    produto = {
        "id": id_contador, 
        "nome": dados.get("nome"), 
        "preco": dados.get("preco"), 
        "categoria": dados.get("categoria")
    }
    produtos_bd.append(produto)
    return jsonify(produto), 201

@app.route("/produtos/<int:id>", methods=["PUT"])
def editarProduto(id):
    dados = request.get_json()
    for produto in produtos_bd:
        if produto["id"] == id:
            produto["nome"] = dados.get("nome")
            produto["preco"] = dados.get("preco")
            produto["categoria"] = dados.get("categoria")
            return jsonify(produto), 200
    return jsonify({"erro": "Produto nao encontrado"}), 404

@app.route("/produtos/<int:id>", methods=["DELETE"])
def removerProduto(id):
    for produto in produtos_bd:
        if produto["id"] == id:
            produtos_bd.remove(produto)
            return "", 204
    return jsonify({"erro": "Produto nao encontrado"}), 404

app.run(debug=True)