# class musica:
#     nome = ''
#     artista = ''
#     duracao = int


# musica1 = musica()
# musica1.nome = "Dont Cry"
# musica1.artista = "Axl Rose"
# musica1.duracao = 455

# musica2 = musica()
# musica2.nome = "Sweat Child no Mine"
# musica2.artista = "Axl Rose"
# musica2.duracao = 766


# musica3 = musica()
# musica3.nome = "Bring Me to Life"
# musica3.artista = "Amy Lee"
# musica3.duracao = 500

#----------------------------------------------

# class restaurante:
#     nome = ''
#     categoria = ''
#     ativo = False


# restaurante_praca = restaurante()
# restaurante_praca.nome = 'Pizza'
# restaurante_praca.categoria = 'Italiana'
# restaurante_praca.ativo = False

# nome = restaurante_praca.nome
# # print(nome)


# # if restaurante_praca.ativo:
# #     print(f"O restaurante {restaurante_praca.nome} está ativo!")
# # else:
# #     print(f"O restaurante {restaurante_praca.nome} não está ativo")

# # categoria = restaurante_praca.categoria

# restaurante_praca.nome = "Bistrô"

# # restaurante_pizza = restaurante
# # restaurante_pizza.nome = 'Pizza Place'
# # restaurante_pizza.categoria = 'Fast Food'
# # restaurante_pizza.ativo = True

# # if restaurante_pizza.categoria == 'Fast Food':
# #     print(f"O restaurante {restaurante_pizza.nome} é da categoria fast food")
# # else:
# #     print(f"O restaurante {restaurante_pizza.nome} não é da categoria fast food")

# print(restaurante_praca.nome)
# print(restaurante_praca.categoria)

#----------------------------------------------

# class Musica():
#     musicas = []
#     nome = ''
#     artista = ''
#     duracao = int

#     def __init__(self, nome, artista, duracao):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = duracao
#         Musica.musicas.append(self)

#     def __str__(self):
#         return f'{self.nome} | {self.artista} | {self.duracao}'

#     def listas_musicas():
#         for musica in Musica.musicas:
#             print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

# musica = Musica("Dont Cry", "Axl Rose", 4)

# Musica.listas_musicas()

#----------------------------------------------


# class Carro():
#     modelo = ''
#     cor = ''
#     ano = int
#     def __init__(self, modelo, cor, ano):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano

# carro1 = Carro("Honda Civic", "Preto", 2010)


# class Restaurante():
#     nome = ''
#     categoria = ''
#     estrelas = int
#     localizacao = ''
#     ativo = False

#     def __init__(self, nome, categoria, estrelas, localizacao, ativo):
#         self.nome = nome
#         self.categoria = categoria
#         self.estrelas = estrelas
#         self.localizacao = localizacao
#         self.ativo = ativo

#     def __str__(self):
#         return f'{self.nome} | {self.categoria} | {self.estrelas} | {self.localizacao} | {self.ativo}'


# restaurante_nativas = Restaurante("Nativas", "Churrascaria", 4, "Asa Sul", True)


# class Cliente():
#     nome = ''
#     sexo = ''
#     telefone = int
#     cpf = int

#     def __init__(self, nome, sexo, telefone, cpf):
#         self.nome = nome
#         self.sexo = sexo
#         self.telefone = telefone
#         self.cpf = cpf

#     def __str__(self):
#         return f'{self.nome} | {self.sexo} | {self.telefone} | {self.cpf}'

# cliente_Erick = Cliente("Erick", "Masculino", 981268974, 7716863150)
# cliente_Maria = Cliente("Maria", "Feminino", 991610516, 7716863150)
# cliente_Alessandra = Cliente("Alessandra", "Feminino", 992440075, 7716863150)

# print(cliente_Maria)
# print(cliente_Erick)
# print(cliente_Alessandra)


#----------------------------------------------

# class Pessoa:
#     nome = ''                                                                                                
#     idade = int
#     profissao = ''

#     def __init__(self,nome, idade, profissao):
#         self.nome = nome
#         self.idade = idade
#         self.profissao = profissao

#     def __str__(self):
#         return f'{self.nome} tem {self.idade} anos, e trabalha com {self.profissao}'

    
#     @property
#     def saudacao(self):
#         return f'Parabéns {self.nome} pelo seu cargo de {self.profissao} e pelos seus {self.idade} anos'

#     def aumentar_idade(self):
#         self.idade += 3

# pessoa = Pessoa('Erick', 18, 'TI')


# pessoa.aumentar_idade()
# print(pessoa.saudacao)

#----------------------------------------------

# class Conta:

#     def __init__(self,tiullar = '', saldo = int):
#         self._tiular = tiullar
#         self._saldo = saldo
#         self._ativo = False

#     def __str__(self):
#         return f' Titular: {self._tiular} | Saldo: {self._saldo} | Ativo: {self._ativo}'

#     def ativar_conta(self):
#         self._ativo = not self._ativo
        
# class conta_pythonica():
#     def __init__(self, titular = '', saldo = int):
#             self._titular = titular
#             self._saldo = saldo
#             self._ativo = False

            
#             self._saldo = saldo

#     @property
#     def titular(self):
#         return self._titular

#     @property
#     def saldo(self):
#         return self._saldo
    
#     @property
#     def ativo(self):
#         return self._ativo


# pessoa1 = Conta("Erick", 5000)
# pessoa2 = Conta("Maria", 4000)
# pessoa3 = conta_pythonica("Luciano", 7000)

# pessoa1.ativar_conta()
# pessoa2.ativar_conta()


# print(pessoa3._titular)

# class Cliente_banco:
#     def __init__(self, nome = '', cpf = int, sexo = '', telefone = int, ativo = False):
#         self._nome = nome
#         self._cpf = cpf
#         self._sexo = sexo
#         self._telefone = telefone
#         self._ativo = ativo

#     def __str__(self):
#         return f' {self._nome} | {self._cpf} | {self._sexo} | {self._telefone} | {self._ativo}'
    
# cliente1 = Cliente_banco('Erick', 7716863150, 'Masculino', 981268974)
# cliente2 = Cliente_banco('Luciano', 5735266672, 'Masculino', 99672187)
# cliente3 = Cliente_banco('Alessandra', 72454490153, 'Feminino', 991610516)

# print(cliente1)
# print(cliente2)
# print(cliente2)

#-------------------------------------------------------------------------------------------

class Livro:
    livros = []
    def __init__(self, titulo = '', autor = '', ano_publicacao = ''):
        self._tiulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        

    def __str__(self):
        return f'{self._tiulo} | {self._autor} | {self._ano_publicacao} | {self._disponivel}'


    def emprestar_livro(self):
        self._disponivel = not self._disponivel

    def verificar_disponiblidade(self):            
        Livro.livros.append(self)
        for livro in Livro.livros:
            print()

livro1 = Livro('Harry Potter e o prisioneiro de askaban', 'Erick', 2004)
livro2 = Livro('O grande conflito', 'Maria', 2023)

livro1.emprestar_livro()
print(livro1)
print(livro2)
