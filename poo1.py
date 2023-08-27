
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocar_cor(self, nova_cor):
        self.cor = nova_cor
    
    def mostrar_cor(self):
        return self.cor


minha_bola = Bola(cor="Azul", circunferencia=25, material="Couro")
print("Cor da bola:", minha_bola.mostrar_cor())

minha_bola.trocar_cor("Verde")
print("Nova cor da bola:", minha_bola.mostrar_cor())


