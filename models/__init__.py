from database import db

emprestimo = db.Table(
    'emprestimo', db.Column('id_emprestimo', db.Integer, db.ForeignKey("leitor.id")), 
    db.Column('id_livro', db.Integer, db.ForeignKey("livro.id"))
)
class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    livros = db.relationship('Livro', backref='autor')

class Leitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    livros = db.relationship('Livro', secondary = emprestimo, backref=db.backref('leitores'))

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100))
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'))
