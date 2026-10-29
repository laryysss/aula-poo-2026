from flask import Flask, request,jsonify

app = Flask (__name__)

id = 0 
aluno_bd = []

@app.route("/alunos")
def retornarAlunos():
    return jsonify(aluno_bd)

@app.route("/alunos", methods=["POST"])
def salvarAluno():
    global id 
    id = id +1 
    dados = request.get_json()
    nome = dados.get("nome")
    curso = dados.get("curso")
    idade = dados.get("idade")
    aluno={"id": id, "nome": nome, "curso": curso, "idade": idade}
    aluno_bd.append(aluno)
    return jsonify(aluno)

@app.route("/alunos/<int: id>", methods=["PUT"])
def editarrAlunos(id):
    dados = request.get_json()
    nome = dados.get("nome")
    curso = dados.get("curso")
    idade = dados.get("idade")
    for aluno in aluno_bd:
        if aluno["id"] == id:
            aluno["nome"] == nome
            curso["curso"] == curso
            idade["idade"] == idade
            return jsonify(aluno), 200
    return jsonify({"erro": "Aluno nao encontrado"}), 404

@app.route("/alunos/<int:id>", methods=["DELETE"])
def removerAluno(id):
    for aluno in aluno_bd:
        if aluno ["id"] == id:
            aluno_bd.remove(aluno)
        return "", 204
    return jsonify({"erro": "aluno nao encontrada"}), 404
app.run(debug=True)


