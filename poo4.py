class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, anos):
        self.idade += anos
        if self.idade < 21:
            self.crescer(0.5 * anos)
    
    def engordar(self, kg):
        self.peso += kg
    
    def emagrecer(self, kg):
        self.peso -= kg
    
    def crescer(self, cm):
        self.altura += cm

nome_pessoa = input("Informe o nome: ")
idade_pessoa = int(input("Informe a idade: "))
peso_pessoa = float(input("Informe o peso: "))
altura_pessoa = float(input("Informe a altura: "))

pessoa = Pessoa(nome_pessoa, idade_pessoa, peso_pessoa, altura_pessoa)

anos_envelhecidos = int(input("Informe quantos anos deseja envelhecer: "))
pessoa.envelhecer(anos_envelhecidos)

print("Idade:", pessoa.idade)
print("Altura:", pessoa.altura)

quilos_engordados = float(input("Informe quantos quilos engordou: "))
pessoa.engordar(quilos_engordados)
print("Peso:", pessoa.peso)

quilos_emagrecidos = float(input("Informe quantos quilos emagreceu: "))
pessoa.emagrecer(quilos_emagrecidos)
print("Peso:", pessoa.peso)
