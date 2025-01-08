from veiculo import Veiculo
class Trem(Veiculo):
    def __init__(self, marca, modelo, ano, nVagoes):
        super().__init__(marca, modelo, ano)
        self.__nVagoes=nVagoes
 
    def setnVagoes(self, vagoes):
        self.__nVagoes=vagoes

    def getnVagoes(self):
        return self.__nVagoes
    
    def mostrar(self):
        return (f'Trem da marca: {self.getMarca()}, Modelo: {self.getModelo()}, Ano: {self.getAno()}, Vagões: {self.getnVagoes()}')
    
#t = Trem('Alstom', 'Monotrilho', 2020, 20)
#print(t.mostrar()) 