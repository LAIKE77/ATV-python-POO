class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
    
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
    
    def alterar_fome(self, novo_valor):
        self.fome = novo_valor
    
    def alterar_saude(self, novo_valor):
        self.saude = novo_valor
    
    def alterar_idade(self, novo_valor):
        self.idade = novo_valor
    
    def retornar_nome(self):
        return self.nome
    
    def retornar_fome(self):
        return self.fome
    
    def retornar_saude(self):
        return self.saude
    
    def retornar_idade(self):
        return self.idade
    
    def calcular_humor(self):
        if self.fome <= 5 and self.saude >= 70:
            return "Feliz"
        elif self.fome <= 10 and self.saude >= 50:
            return "Neutro"
        else:
            return "Triste"


nome_bichinho = input("Informe o nome do Bichinho: ")
fome_bichinho = int(input("Informe o nível de fome do Bichinho Virtual (0-10): "))
saude_bichinho = int(input("Informe o nível de saúde do Bichinho Virtual (0-100): "))
idade_bichinho = int(input("Informe a idade do Bichinho: "))

bichinho = BichinhoVirtual(nome_bichinho, fome_bichinho, saude_bichinho, idade_bichinho)

print("Humor:", bichinho.calcular_humor())
