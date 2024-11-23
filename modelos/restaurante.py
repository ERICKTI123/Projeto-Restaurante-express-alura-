from modelos.avaliacao import Avaliacao # importando o arquivo avaliacao.py

class Restaurante: # representa um restaurante e suas caracteristicas 
    restaurantes = []

    def __init__(self, nome, categoria): # metodo construtor 
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    

    def __str__(self): # retorna o objeto em forma de string
        return f'{self._nome} | {self._categoria} | {self.ativo}'


    # função que lista todos os restaurantes, utilizando também o metodo de classe
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} {'Categoria do restaurante'.ljust(25)} {'Situação do restaurante'.ljust(25)} {'Avaliação do Restaurante'}")
        for restaurante in cls.restaurantes:

            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {restaurante.media_avaliacoes}")
 
    # muda a visualização do atributo ativo, utilizando também o property
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'

    # muda o estado do ativo
    def alternar_estado(self):
        self._ativo = not self._ativo

    # função que recebe as avaliações
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    # Calculando a média de avaliações 
    @property   
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade = len(self._avaliacao)
        media = round(notas / quantidade,1)
        return media
    

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza", "Italiana")

restaurante_praca.alternar_estado()
restaurante_pizza.alternar_estado()





