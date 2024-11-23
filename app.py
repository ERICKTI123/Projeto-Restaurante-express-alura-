from modelos.restaurante import Restaurante # importando o arquivo restaurante.py 
from modelos.avaliacao import Avaliacao # importando o arquivo avaliacao.py

restaurante_pizza = Restaurante("Pizza", "Gourmet") # nome e categoria do restaurante
restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.receber_avaliacao("nome", 10)
restaurante_praca.receber_avaliacao("nome", 8)
restaurante_praca.receber_avaliacao("nome", 5)
# recebendo as avaliações

# Função que lista todos os atributos do restaurante
def main():
    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()