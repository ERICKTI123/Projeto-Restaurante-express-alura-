class Avaliacao: # Criano a classe avaliação que têm os parâmetros cliente e nota
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota

    # retorna o obeto avaliação em forma de string
    def __str__(self):
        return f"Cliente: {self._cliente}, Nota: {self._nota}"