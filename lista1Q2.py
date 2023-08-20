"""
Classe Quadrado: Crie uma classe que modele um quadrado: a. Atributos: tamanholado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Area:
"""
class Quadrado:
    'Classe que modela um quadrado'
    tamanhoLado = 0.0

    def mostraLado(self):
        print(self.tamanhoLado)

    def mudar(self, nlado):
        self.tamanhoLado = nlado
    
    def area(self):
        print('O tamho da área é:', self.tamanhoLado**2)

# Exemplo 
quadrado1 = Quadrado()
quadrado1.mostraLado()
quadrado1.mudar(4)
quadrado1.mostraLado()
quadrado1.area