from veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, nPortas):
        super().__init__(marca, modelo, ano)
        self.__nPortas=nPortas
 
    def setnPortas(self, portas):
        self.__nPortas=portas

    def getNPortas(self):
        return self.__nPortas
    
    def mostrar(self):
        return (f'Carro da marca: {self.getMarca()}, Modelo: {self.getModelo()}, Ano: {self.getAno()}, Portas: {self.getNPortas()}')
    
#c = Carro('VW', 'Gol' , 2000, 5)
#print(c.mostrar()) 