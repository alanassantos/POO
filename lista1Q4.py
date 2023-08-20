"""Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
b. Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que
nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5

"""
class Pessoa:
    'Classe que modela uma pessoa'
    def __init__(self, nome, idade, alturacm, peso):
        self.nome = nome 
        self.idade = idade
        self.altura = alturacm
        self.peso = peso 

    def engordar(self, quilos):
        self.peso += quilos
        return self.peso

    def emagrecer(self, quilos_perder):
        self.peso -= quilos_perder
        return self.peso

    def envelhecer(self, anos):
        self.idade += anos
        return self.idade

    def crescer(self, anos):
        if self.idade < 21:
            self.altura += (0.5 * anos)
        return self.altura
        
def main():
    n = input('Digite o nome da pessoa:     ')
    i = int(input('Digite a idade:    '))
    a = float(input('Digite a altura:    '))
    p = float(input('Digite o peso:     '))

    pessoa1 = Pessoa(n, i, a, p)
    print(f'O nome da pessoa é {pessoa1.nome}, sua idade é {pessoa1.idade}, sua altura é {pessoa1.altura}, seu peso {pessoa1.peso}')

    while True:
        a = input('Digite os comandos abaixo para fazer com a pessoa \n0 - Engordar \n1 - Emagrecer \n2 - Envelhecer \n3 - Crescer \n4 - Sair \n')
        if a == '0':
            k = float(input('Digite a quantidade quilos que deseja engordar a pessoa:   '))
            pessoa1.engordar(k)
        elif a == "1":
            e = float(input('Digite a quantidade de quilos que deseja emagrecer a pessoa:   '))
            pessoa1.emagrecer(e)
        elif a == '2':
            en = int(input('Digite a quantidade de anos que deseja envelhecer:  '))
            pessoa1.envelhecer(en)
        elif a == '3':
            c = int(input('Digite a quantidade de anos que deseja crescer:  '))
            pessoa1.crescer(c)
        elif a == '4':
            break
        else:
            print('Digite um comando válido')
    
    
    print(f'Após interagir com {pessoa1.nome}, seus atributos agora são: \nIdade: {pessoa1.idade} \nAltura: {pessoa1.altura} \nPeso: {pessoa1.peso}')

if __name__ =="__main__":
    main()
