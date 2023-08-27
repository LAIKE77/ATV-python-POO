class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
    
    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome
    
    def depósito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

numero_conta = input("Informe o número da conta: ")
nome_correntista = input("Informe o nome do correntista: ")
saldo_inicial = float(input("Informe o saldo inicial (opcional, padrão é 0): "))

conta = ContaCorrente(numero_conta, nome_correntista, saldo_inicial)

print("Nome do correntista:", conta.nome_correntista)
novo_nome = input("Informe o novo nome do correntista: ")
conta.alterarNome(novo_nome)
print("Novo nome do correntista:", conta.nome_correntista)

valor_deposito = float(input("Informe o valor do depósito: "))
conta.depósito(valor_deposito)
print("Novo saldo:", conta.saldo)

valor_saque = float(input("Informe o valor do saque: "))
conta.saque(valor_saque)
print("Novo saldo:", conta.saldo)
