class Usuario:
    def __init__(self, matricula, nome, tipo, email):
        self.matricula = matricula
        self.nome = nome
        self.tipo = tipo
        self.email = email
        
    def __str__(self):
        return "%s - %s" % (self.matricula, self.nome)