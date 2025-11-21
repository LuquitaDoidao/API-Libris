import fdb

class acervo:
    def __init__(self, id_livro, titulo, autor, categoria, isbn, qtd_disponivel, sinopse, idioma, ano_publicado):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        self.qtd_disponivel = qtd_disponivel
        self.sinopse = sinopse
        self.idioma = idioma
        self.ano_publicado = ano_publicado

class usuario:
    def __init__(self, id_usuario, nome, email, telefone, endereco, senha, tipo, ativo, data_nascimento):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.senha = senha
        self.tipo = tipo
        self.ativo = ativo
        self.data_nascimento = data_nascimento