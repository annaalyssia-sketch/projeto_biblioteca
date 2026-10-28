from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Autor, Livro, Leitor

rotas = Blueprint('rotas', __name__)

@rotas.route('/', methods = ["GET", "POST"])
def inicio():
    if request.method == "POST":
        tipo = request.form["tipo"]

        if tipo == "autor":
            nome = request.form["nome"]
            db.session.add(Autor(nome=nome))

        elif tipo == "livro":
            titulo = request.form["titulo"]
            autor_id = request.form["autor_id"]
            db.session.add(Livro(titulo=titulo, autor_id=int(autor_id)))

        elif tipo == "leitor":
            nome = request.form["nome"]
            db.session.add(Leitor(nome=nome))

        elif tipo == "emprestimo":
            leitor = db.session.get(Leitor, int(request.form["leitor_id"]))
            livro = db.session.get(Livro, int(request.form["livro_id"]))
            if livro not in leitor.livros:
                leitor.livros.append(livro)

        elif tipo == "excluir_autor":
            autor = db.session.get(Autor, int(request.form["autor_id"]))
            if autor and not autor.livros:
                db.session.delete(autor)

        elif tipo == "excluir_livro":
            livro = db.session.get(Livro, int(request.form["livro_id"]))
            
            if livro and not livro.leitores:
                db.session.delete(livro)

        elif tipo == "excluir_leitor":
            leitor = db.session.get(Leitor, int(request.form["leitor_id"]))
            if leitor and not leitor.livros:
                db.session.delete(leitor)

        db.session.commit()
        return redirect(url_for('rotas.inicio'))
    
    return render_template('index.html', autores=Autor.query.all(), livros=Livro.query.all(), leitores=Leitor.query.all())  