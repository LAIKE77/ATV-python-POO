class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 50
    
    def mudar_canal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido!")
    
    def aumentar_volume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume máximo atingido!")
    
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume mínimo atingido!")
    
    def mostrar_informacoes(self):
        print("Canal:", self.canal)
        print("Volume:", self.volume)


def main():
    tv = TV()
    
    while True:
        print("\n--- Controle Remoto da TV ---")
        print("1. Mudar Canal")
        print("2. Aumentar o Volume")
        print("3. Diminuir o Volume")
        print("4. Mostrar as Informações da TV")
        print("0. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            novo_canal = int(input("Informe o novo número do canal: "))
            tv.mudar_canal(novo_canal)
        elif opcao == 2:
            tv.aumentar_volume()
        elif opcao == 3:
            tv.diminuir_volume()
        elif opcao == 4:
            tv.mostrar_informacoes()
        elif opcao == 0:
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
