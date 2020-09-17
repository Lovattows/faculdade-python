class Usuario:
    def __init__(self, matricula, nome, tipo, email):
        self.matricula = matricula
        self.nome = nome
        self.tipo = tipo
        self.email = email

    def __str__(self):
        return "Matrícula: %s\nNome: %s\nTipo: %s\nE-mail: %s\n\n" % (self.matricula, self.nome, self.tipo, self.email)
