from flask import Flask, request, jsonify

app = Flask(__name__)

id_contador = 0 
funcionarios_bd = []

@app.route("/funcionarios")
def retornarFuncionarios():
    return jsonify(funcionarios_bd), 200

@app.route("/funcionarios", methods=["POST"])
def salvarFuncionario():
    global id_contador 
    id_contador += 1 
    dados = request.get_json()
    funcionario = {
        "id": id_contador, 
        "nome": dados.get("nome"), 
        "cargo": dados.get("cargo"), 
        "salario": dados.get("salario")
    }
    funcionarios_bd.append(funcionario)
    return jsonify(funcionario), 201

@app.route("/funcionarios/<int:id>", methods=["PUT"])
def editarFuncionario(id):
    dados = request.get_json()
    for funcionario in funcionarios_bd:
        if funcionario["id"] == id:
            funcionario["nome"] = dados.get("nome")
            funcionario["cargo"] = dados.get("cargo")
            funcionario["salario"] = dados.get("salario")
            return jsonify(funcionario), 200
    return jsonify({"erro": "Funcionario nao encontrado"}), 404

@app.route("/funcionarios/<int:id>", methods=["DELETE"])
def removerFuncionario(id):
    for funcionario in funcionarios_bd:
        if funcionario["id"] == id:
            funcionarios_bd.remove(funcionario)
            return "", 204
    return jsonify({"erro": "Funcionario nao encontrado"}), 404

app.run(debug=True)