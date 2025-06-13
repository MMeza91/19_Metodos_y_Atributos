import ingredientes as ingre

class Pizza():
    tamano = "Familiar"
    precio = 10000

    @staticmethod
    def validar(elemento:str, lista:list[str]):
        return True if elemento in lista else False
    
    def realizar_pedido(self):
        ingredientes = []
        #pedir 2 ingredientes vegetales y 1 de carne
        #validar datos ingresados
        #entregar respuesta a ingredientes = []
        