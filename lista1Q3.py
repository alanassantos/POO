"""
Classe Retangulo: Crie uma classe que modele um retângulo: 
a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher) 
b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular perimetro; 
c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local. Depois, deve criar um objeto 
com as medidas fornecidas e outro objeto com medidas de um piso. O programa deve calcular a quantidade de pisos necessários para o local.
"""
class Retangulo:
    "Classe que modela um retângulo"
    LadoA = 0.0
    LadoB = 0.0

    def mudar_lado(self, nladoA, nladoB):
        self.LadoA = nladoA
        self.LadoB = nladoB
    
    def retorna(self):
        print('O valor do Lado A é:', self.LadoA)
        print('O valor do Ldo B:', self.LadoB)

    def area(self):
        return(self.LadoA * self.LadoB)

    def perimetro(self):
        return(self.LadoA * 2 + self.LadoB * 2)

def main():
    base = float(input('Digite o tamanho do lado A:     '))
    altura = float(input('Digite o tamanho do Lado B:   '))

    comprimento = float(input('Digite a altura do piso:     '))
    largura = float(input('Digite a largura do piso:    '))

    retangulo1 = Retangulo()
    retangulo1.mudar_lado(base, altura)
    print(f"O valor da área do retângulo é {retangulo1.area()}")
    print(f'O valor do perímetro do retângilo é {retangulo1.perimetro()}')

    piso = Retangulo()
    piso.mudar_lado(comprimento, largura)

    quantidade = retangulo1.area() / piso.area()

    print(f"A quantidade de pisos necessárias é igual {quantidade}") 

if __name__ =="__main__":
    main()
