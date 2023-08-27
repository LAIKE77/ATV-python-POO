class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
    
    def comer(self, alimento):
        self.bucho.append(alimento)
    
    def ver_bucho(self):
        print(f"Conteúdo do estômago de {self.nome}: {self.bucho}")
    
    def digerir(self):
        self.bucho = []
        print(f"{self.nome} digeriu o alimento.")


def main():
    macaco1 = Macaco("Macaco A")
    macaco2 = Macaco("Macaco B")
    
    print("Alimentando Macaco A...")
    macaco1.comer("Banana")
    macaco1.comer("Maçã")
    macaco1.comer("Nozes")
    macaco1.ver_bucho()
    
    print("\nAlimentando Macaco B...")
    macaco2.comer("Folhas")
    macaco2.comer("Pão")
    macaco2.comer("Cenoura")
    macaco2.ver_bucho()
    
    print("\nDigerindo Macaco A...")
    macaco1.digerir()
    macaco1.ver_bucho()
    
    print("\nDigerindo Macaco B...")
    macaco2.digerir()
    macaco2.ver_bucho()

if __name__ == "__main__":
    main()
