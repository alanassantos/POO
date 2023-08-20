"""
Classe Bola: Crie uma classe que modele uma bola:
a. Atributos: cor, circunferencia, material
b. Métodos: trocaCor e mostraCor
"""

#Criando a classe Bola e os atributos
class Bola:
    "Classe que modela uma bola"
    cor = 'Sem cor'
    circuferencia = 0.0 
    material = 'Sem material'

    def trocaCor(self, novaCor):
        self.cor = novaCor

    def mostraCor(self):
        print(self.cor)

# Criando o objeto
bola1 = Bola()
bola1.mostraCor()
bola1.trocaCor('Vermelho')
bola1.mostraCor()