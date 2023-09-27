"""
Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: __nome, endereço, __telefone, __idade, dataNascimento 
b. Métodos: __init__, getters e setters, __str__, serProcessada por uma Pessoa – perceba que este método deve receber um objeto do tipo Pessoa.
"""
class Pessoa:
    '''Classe que modela uma pessoa'''
    def __init__(self,nome,endereco,telefone,idade, dataNascimento):
        self.__nome = nome
        self.endereco = endereco
        self.__telefone = telefone
        self.__idade = idade
        self.dataNascimento = dataNascimento
        self.pessoasQueProcessam = []

    def get_Nome(self):
        return self.__nome
    
    def set_Nome(self, Novonome):
        self.__nome = Novonome
    
    def get_Telefone(self):
        return self.__telefone
    
    def set_Telefone(self, NovoTelefone):
        self.__telefone = NovoTelefone

    def get_Telefone(self):
        return self.__telefone 
    
    def get_idade(self):
        return self.__idade
    
    def set_idade(self, NovaIdade):
        self.__idade = NovaIdade

    def serProcessada(self, outraPessoa):
        if type(outraPessoa) == Pessoa:
            self.pessoasQueProcessam.append(outraPessoa)
        else:
            print('Digite um objeto')
        for pessoa in self.pessoasQueProcessam:
            print(f'Pessoas que me processam: {pessoa.get_Nome()}')

    def nome(self):
        return self.nome

    def __str__(self):
        return f'{"*"*6} Pessoas {"*"*6}\nNome: {self.__nome}\nEndereço: {self.endereco}\nTelefone: {self.__telefone}\nIdade: {self.__idade}\nData Nascimento: {self.dataNascimento}'
    
if __name__ == '__main__':

    Maria = Pessoa('Maria', 'Rua muiatuca', 22243535, 23, "23/09/2002")
    print(Maria)
    João = Pessoa('João', 'Estrada 24', 232947297, 23, "09/08/2000")
    print(João)
    Maria.serProcessada(João)
    print(João.get_Nome())

    print("**"*9)
