class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def mudar_lado(self, novo_lado):
        self.lado = novo_lado
    
    def retornar_lado(self):
        return self.lado
    
    def calcular_area(self):
        return self.lado ** 2

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
    
    def mudar_lados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b
    
    def retornar_lados(self):
        return self.lado_a, self.lado_b
    
    def calcular_area(self):
        return self.lado_a * self.lado_b
    
    def calcular_perimetro(self):
        return 2 * (self.lado_a + self.lado_b)


def main():
    lado_local = float(input("Informe o tamanho do lado da aréa: "))
    largura_local = float(input("Informe a largura do aréa: "))
    comprimento_local = float(input("Informe o comprimento da aréa: "))
    
    area_local = largura_local * comprimento_local
    
    quadrado_piso = Quadrado(lado_local)
    retangulo_rodape = Retangulo(largura_local, lado_local)
    
    quantidade_pisos = area_local / quadrado_piso.calcular_area()
    quantidade_rodapes = 2 * (largura_local + comprimento_local) / retangulo_rodape.calcular_perimetro()
    
    print("Quantidade de pisos:", quantidade_pisos)
    print("Quantidade de rodapés:", quantidade_rodapes)

if __name__ == "__main__":
    main()
