class Ata:
    def __init__(self, numero, data, hora, local, pauta, redator, lista_integrantes, texto, validade):
        self.numero = numero
        self.data = data
        self.hora = hora
        self.local = local
        self.pauta = pauta
        self.redator = redator
        self.lista_integrantes = lista_integrantes
        self.texto = texto
        self.validade = validade

    def __str__(self):
        return "Número: %s\nData: %s\nHora: %s\nLocal: %s\nPauta: %s\nRedator: %s\nLista Integrantes: %s\nTexto: " \
               "%s\nValidade: %s\n\n" % (self.numero, self.data, self.hora, self.local, self.pauta,
                                         self.redator, self.lista_integrantes, self.texto, self.validade)
