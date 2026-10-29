from flask import Flask, request, jsonify

app = Flask(__name__)

id_contador = 0 
cursos_bd = []

@app.route("/cursos")
def retornarCursos():
    return jsonify(cursos_bd), 200

@app.route("/cursos", methods=["POST"])
def salvarCurso():
    global id_contador 
    id_contador += 1 
    dados = request.get_json()
    curso = {
        "id": id_contador, 
        "nome": dados.get("nome"), 
        "instituicao": dados.get("instituicao"), 
        "duracao": dados.get("duracao")
    }
    cursos_bd.append(curso)
    return jsonify(curso), 201

@app.route("/cursos/<int:id>", methods=["PUT"])
def editarCurso(id):
    dados = request.get_json()
    for curso in cursos_bd:
        if curso["id"] == id:
            curso["nome"] = dados.get("nome")
            curso["instituicao"] = dados.get("instituicao")
            curso["duracao"] = dados.get("duracao")
            return jsonify(curso), 200
    return jsonify({"erro": "Curso nao encontrado"}), 404

@app.route("/cursos/<int:id>", methods=["DELETE"])
def removerCurso(id):
    for curso in cursos_bd:
        if curso["id"] == id:
            cursos_bd.remove(curso)
            return "", 204
    return jsonify({"erro": "Curso nao encontrado"}), 404


app.run(debug=True)