import json
import os
import uuid

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)


UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
MAX_FILE_SIZE = 4 * 1024 * 1024

app.config["MAX_CONTENT_LENGTH"] = MAX_FILE_SIZE


def carregar_alunos():
    with open("alunos.json", "r", encoding="utf-8") as arquivo:
        alunos = json.load(arquivo)

    alunos.sort(key=lambda aluno: aluno["nome"].lower())

    return alunos


def salvar_alunos(alunos):
    with open("alunos.json", "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)


def extensao_permitida(nome_arquivo):
    if "." not in nome_arquivo:
        return False

    extensao = nome_arquivo.rsplit(".", 1)[1].lower()

    return extensao in ALLOWED_EXTENSIONS


def salvar_foto(arquivo):
    if not arquivo or not arquivo.filename:
        return None

    if not extensao_permitida(arquivo.filename):
        return None

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    extensao = arquivo.filename.rsplit(".", 1)[1].lower()

    nome_arquivo = f"{uuid.uuid4().hex}.{extensao}"

    caminho = os.path.join(UPLOAD_FOLDER, nome_arquivo)

    arquivo.save(caminho)

    return nome_arquivo


def excluir_foto(foto):
    if not foto:
        return

    caminho = os.path.join(UPLOAD_FOLDER, foto)

    if os.path.exists(caminho):
        os.remove(caminho)


@app.route("/")
def home():
    alunos = carregar_alunos()

    return render_template("index.html", alunos=alunos)


@app.route("/alunos")
def lista_alunos():
    alunos = carregar_alunos()

    busca = request.args.get("busca", "").strip()

    if busca:
        alunos = [
            aluno
            for aluno in alunos
            if busca.lower() in aluno["nome"].lower()
        ]

    return render_template(
        "alunos.html",
        alunos=alunos,
        busca=busca
    )


@app.route("/alunos/<nome>")
def detalhes_aluno(nome):
    alunos = carregar_alunos()

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return render_template(
                "aluno.html",
                aluno=aluno
            )

    return "Aluno não encontrado!", 404


@app.route("/cadastrar")
def pagina_cadastrar():
    return render_template("cadastrar.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    alunos = carregar_alunos()

    nome = request.form["nome"].strip()

    if not nome:
        return render_template(
            "cadastrar.html",
            mensagem="Digite um nome válido!"
        )

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return render_template(
                "cadastrar.html",
                mensagem="Aluno já cadastrado!"
            )

    foto = salvar_foto(request.files.get("foto"))

    if request.files.get("foto") and request.files.get("foto").filename and foto is None:
        return render_template(
            "cadastrar.html",
            mensagem="Formato de foto inválido! Use PNG, JPG, JPEG ou WEBP."
        )

    alunos.append({
        "nome": nome,
        "foto": foto,
        "notas": []
    })

    salvar_alunos(alunos)

    return render_template(
        "cadastrar.html",
        mensagem="Aluno cadastrado com sucesso!"
    )


@app.route("/editar/<nome>", methods=["GET", "POST"])
def editar_aluno(nome):
    alunos = carregar_alunos()

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            if request.method == "POST":

                novo_nome = request.form["nome"].strip()

                if not novo_nome:
                    return render_template(
                        "editar.html",
                        aluno=aluno,
                        mensagem="Digite um nome válido!"
                    )

                for outro_aluno in alunos:
                    if (
                        outro_aluno is not aluno
                        and outro_aluno["nome"].lower() == novo_nome.lower()
                    ):
                        return render_template(
                            "editar.html",
                            aluno=aluno,
                            mensagem="Já existe um aluno com esse nome!"
                        )

                arquivo_foto = request.files.get("foto")
                remover_foto = request.form.get("remover_foto")

                if remover_foto == "1":
                    excluir_foto(aluno.get("foto"))
                    aluno["foto"] = None

                elif arquivo_foto and arquivo_foto.filename:

                    nova_foto = salvar_foto(arquivo_foto)

                    if nova_foto is None:
                        return render_template(
                            "editar.html",
                            aluno=aluno,
                            mensagem="Formato de foto inválido! Use PNG, JPG, JPEG ou WEBP."
                        )

                    excluir_foto(aluno.get("foto"))

                    aluno["foto"] = nova_foto

                aluno["nome"] = novo_nome

                salvar_alunos(alunos)

                return redirect(
                    url_for(
                        "detalhes_aluno",
                        nome=novo_nome
                    )
                )

            return render_template(
                "editar.html",
                aluno=aluno
            )

    return "Aluno não encontrado!", 404


@app.route("/excluir/<nome>", methods=["POST"])
def excluir_aluno(nome):
    alunos = carregar_alunos()

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            excluir_foto(aluno.get("foto"))

            alunos.remove(aluno)

            salvar_alunos(alunos)

            return redirect(
                url_for("lista_alunos")
            )

    return "Aluno não encontrado!", 404


@app.route("/notas")
def notas():
    alunos = carregar_alunos()

    return render_template(
        "notas.html",
        alunos=alunos
    )


@app.route("/adicionar-nota", methods=["POST"])
def adicionar_nota():
    alunos = carregar_alunos()

    nome = request.form["nome"].strip()

    try:
        nota = float(request.form["nota"])

    except ValueError:
        return render_template(
            "notas.html",
            alunos=alunos,
            mensagem="Digite uma nota válida!"
        )

    if nota < 0 or nota > 10:
        return render_template(
            "notas.html",
            alunos=alunos,
            mensagem="A nota deve estar entre 0 e 10!"
        )

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            aluno["notas"].append(nota)

            salvar_alunos(alunos)

            return render_template(
                "notas.html",
                alunos=alunos,
                mensagem="Nota adicionada com sucesso!"
            )

    return render_template(
        "notas.html",
        alunos=alunos,
        mensagem="Aluno não encontrado!"
    )


@app.route("/editar-nota/<nome>/<int:indice>", methods=["GET", "POST"])
def editar_nota(nome, indice):
    alunos = carregar_alunos()

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            if indice < 0 or indice >= len(aluno["notas"]):
                return "Nota não encontrada!", 404

            if request.method == "POST":

                try:
                    nova_nota = float(request.form["nota"])

                except ValueError:
                    return render_template(
                        "editar_nota.html",
                        aluno=aluno,
                        indice=indice,
                        nota=aluno["notas"][indice],
                        mensagem="Digite uma nota válida!"
                    )

                if nova_nota < 0 or nova_nota > 10:
                    return render_template(
                        "editar_nota.html",
                        aluno=aluno,
                        indice=indice,
                        nota=aluno["notas"][indice],
                        mensagem="A nota deve estar entre 0 e 10!"
                    )

                aluno["notas"][indice] = nova_nota

                salvar_alunos(alunos)

                return redirect(
                    url_for(
                        "detalhes_aluno",
                        nome=aluno["nome"]
                    )
                )

            return render_template(
                "editar_nota.html",
                aluno=aluno,
                indice=indice,
                nota=aluno["notas"][indice]
            )

    return "Aluno não encontrado!", 404


@app.route("/excluir-nota/<nome>/<int:indice>", methods=["POST"])
def excluir_nota(nome, indice):
    alunos = carregar_alunos()

    for aluno in alunos:

        if aluno["nome"].lower() == nome.lower():

            if indice < 0 or indice >= len(aluno["notas"]):
                return "Nota não encontrada!", 404

            aluno["notas"].pop(indice)

            salvar_alunos(alunos)

            return redirect(
                url_for(
                    "detalhes_aluno",
                    nome=aluno["nome"]
                )
            )

    return "Aluno não encontrado!", 404


@app.errorhandler(413)
def arquivo_muito_grande(error):
    alunos = carregar_alunos()

    return render_template(
        "cadastrar.html",
        mensagem="A foto é muito grande! O tamanho máximo é 4 MB.",
        alunos=alunos
    ), 413


if __name__ == "__main__":
    app.run(debug=True)