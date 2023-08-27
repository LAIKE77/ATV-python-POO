class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self, valor_abastecido):
        litros_abastecidos = valor_abastecido / self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        return litros_abastecidos
    
    def abastecer_por_litro(self, litros_abastecidos):
        valor_a_pagar = litros_abastecidos * self.valor_litro
        self.quantidade_combustivel -= litros_abastecidos
        return valor_a_pagar
    
    def alterar_valor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro
    
    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel
    
    def alterar_quantidade_combustivel(self, nova_quantidade_combustivel):
        self.quantidade_combustivel = nova_quantidade_combustivel


def main():
    bomba = BombaCombustivel("Gasolina", 5.0, 1000)
    
    while True:
        print("\nMenu:")
        print("1. Abastecer por valor")
        print("2. Abastecer por litro")
        print("3. Alterar valor do litro")
        print("4. Alterar tipo de combustível")
        print("5. Alterar quantidade de combustível")
        print("0. Sair")
        
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            valor_abastecido = float(input("Informe o valor a ser abastecido: "))
            litros_abastecidos = bomba.abastecer_por_valor(valor_abastecido)
            print(f"Foram abastecidos {litros_abastecidos:.2f} litros.")
        elif opcao == 2:
            litros_abastecidos = float(input("Informe a quantidade em litros a ser abastecida: "))
            valor_a_pagar = bomba.abastecer_por_litro(litros_abastecidos)
            print(f"Valor a pagar: R${valor_a_pagar:.2f}")
        elif opcao == 3:
            novo_valor_litro = float(input("Informe o novo valor do litro: "))
            bomba.alterar_valor(novo_valor_litro)
        elif opcao == 4:
            novo_tipo_combustivel = input("Informe o novo tipo de combustível: ")
            bomba.alterar_combustivel(novo_tipo_combustivel)
        elif opcao == 5:
            nova_quantidade_combustivel = float(input("Informe a nova quantidade de combustível: "))
            bomba.alterar_quantidade_combustivel(nova_quantidade_combustivel)
        elif opcao == 0:
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
