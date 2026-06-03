class Pet:
    def __init__(self,nome, humor):
        self._nome = nome
        self._humor = humor
    
    def brincar(self):
        self._humor +=1

    def mostrar_status(self):
        print(f"o pet {self._nome} está com o humor de {self._humor}")
        

class CaoRobo(Pet):
    def __init__(self, nome, humor, carga_bateria):
        super().__init__(nome,humor)
        self.carga = carga_bateria

    def carregar_bateria(self, valor):
        self.carga += valor

class Dragao(Pet):
    def __init__(self, nome, humor, nivel_fogo ):
        super().__init__(nome,humor)
        self.fogo = nivel_fogo

    def soltar_fogo(self):
        self._humor -= 1
        self.fogo += 1


cao = CaoRobo('Bob', 10, 80)
cao.brincar()
cao.carregar_bateria(5)
cao.mostrar_status()

dragao = Dragao('Spike', 5, 12 )
dragao.brincar()
dragao.soltar_fogo()
dragao.mostrar_status()