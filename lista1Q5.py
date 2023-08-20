'''
Classe Plataforma: Crie uma classe que represente uma plataforma de petróleo: 
a. Atributos: identificação (id), tipo de extração, localização, quantidade da tripulação 
b. Métodos: perfurar, extrair petróleo, extrair gás, lançar âncoras, preparar para carregamento/descarregamento
'''

class Plataforma:
    "Classe que modela uma plataforma de petróleo"

    def __init__(self, id, extracao, localizacao, q_tripulacao):
        self.id = id
        self.extracao = extracao
        self.localizacao = localizacao
        self.tripulacao = q_tripulacao

    def mostrar(self):
        print(f'Plataforma:\nIdentificação: {self.id} \nTipo de extração: {self.extracao} \nLocalização: {self.localizacao} \nQuantidadde de Tripulantes: {self.tripulacao}')
    def perfurar(self):
        print('Perfurando...')

    def extrair(self):
        print('Extraindo petróleo...')

    def extair_gas(self):
        print('Extraindo gás...')
    
    def lançar(self):
        print('Lançar âncoras...')

    def preparar(self):
        print('Preparar para carregamento / descarregamento...')

# Exemplo:
plataforma1 = Plataforma('P123', 'Offshore', 'RJ', 35)
plataforma1.mostrar()
plataforma1.perfurar()
plataforma1.preparar()

