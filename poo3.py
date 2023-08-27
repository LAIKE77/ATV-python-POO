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
    largura_local = float(input("Informe a largura da aréa: "))
    comprimento_local = float(input("Informe o comprimento da aréa: "))
    
    retangulo_local = Retangulo(largura_local, comprimento_local)
    
    area_local = retangulo_local.calcular_area()
    perimetro_local = retangulo_local.calcular_perimetro()
    
    tamanho_piso = float(input("Informe o tamanho do lado do piso: "))
    
    quantidade_pisos = area_local / (tamanho_piso ** 2)
    quantidade_rodapes = perimetro_local / tamanho_piso
    
    print("Quantidade de pisos:", quantidade_pisos)
    print("Quantidade de rodapés:", quantidade_rodapes)

if __name__ == "__main__":
    main()
