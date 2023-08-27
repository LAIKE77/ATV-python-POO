class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir(self):
        print(f"Ponto: ({self.x}, {self.y})")

class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura
    
    def centro(self):
        centro_x = self.ponto_inicial.x + self.largura / 2
        centro_y = self.ponto_inicial.y + self.altura / 2
        return Ponto(centro_x, centro_y)

def main():
    ponto_inicial = Ponto(2, 3)
    retangulo = Retangulo(ponto_inicial, 5, 4)
    
    while True:
        print("\nMenu:")
        print("1. Alterar valores do retângulo")
        print("2. Imprimir o centro do retângulo")
        print("0. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            novo_x = int(input("Informe o novo valor de x para o ponto inicial: "))
            novo_y = int(input("Informe o novo valor de y para o ponto inicial: "))
            nova_largura = int(input("Informe a nova largura do retângulo: "))
            nova_altura = int(input("Informe a nova altura do retângulo: "))
            
            ponto_inicial = Ponto(novo_x, novo_y)
            retangulo = Retangulo(ponto_inicial, nova_largura, nova_altura)
        elif opcao == 2:
            centro = retangulo.centro()
            centro.imprimir()
        elif opcao == 0:
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
