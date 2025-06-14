import ingredientes as ingre

#1. En el archivo pizza.py, crear una clase que permita crear objetos de tipo Pizza. Considerar qué atributos de clase debe contener la clase, según la descripción del problema.

class Pizza():
    tamano = "Familiar"
    precio = 10000

#2. En el mismo archivo y clase del requerimiento anterior, agregar un método que permita validar un elemento dentro de una lista de casos posibles. Este método se debe poder utilizar sin necesidad de crear un objeto de la clase, y debe recibir 2 argumentos:
#a. El elemento a validar (un texto).
#b. Los valores posibles a considerar para el elemento ingresado (una lista de textos).
#En caso de que el elemento ingresado como primer argumento se encuentre entre la lista de valores posibles ingresada como segundo argumento, el método debe retornar True. En caso contrario, debe retornar False.

    @staticmethod
    def validar(elemento:str, lista:list[str]):
        return True if elemento in lista else False
    
#3. En el mismo archivo y clase del requerimiento anterior, agregar un método que permita realizar un pedido. Para ello, dentro de la definición de este método, 
# debe solicitar al usuario ingresar el ingrediente proteico, luego el primer ingrediente vegetal, luego el segundo ingrediente vegetal, y finalmente el tipo de masa. Cada ingreso debe almacenarse (o añadirse, si corresponde) en un atributo de la instancia.
    
    def realizar_pedido(self):
        print()
        print("Los ingredientes con alto contenido de proteínas son:")
        for ingrediente in ingre.proteico:
            print(ingrediente)
        print()
        self.proteina = input("Ingrese su Proteína seleccionada: ")
        print()
        print("Los ingredientes vegetales son:")
        for ingrediente in ingre.vegetal:
            print(ingrediente)
        print()
        self.verdura_1 = input("Ingrese su primera Verdura seleccionada: ")
        self.verdura_2 = input("Ingrese su segunda Verdura seleccionada: ")
        print()
        print("Los tipos de masa son:")
        for ingrediente in ingre.masa:
            print(ingrediente)
        print()
        self.masa = input("Ingrese su Masa seleccionada: ")
        

        
        
        
        

    #4. Dentro del mismo método del requerimiento 3, una vez asignados los valores a los atributos de la instancia, debe evaluarse si se trata de un ingreso válido (considerar la información de la descripción), usando el método del requerimiento 2. Si los 3 ingredientes y el tipo de masa son válidos, deberá almacenar en un atributo el valor True. En caso contrario, deberá almacenar el valor False. Este atributo permitirá saber si una instancia específica es o no una Pizza válida.
        
        self.pizza_valida = self.validar(self.proteina, ingre.proteico) and self.validar(self.verdura_1 ,ingre.vegetal) and self.validar(self.verdura_2 ,ingre.vegetal) and self.validar(self.masa ,ingre.masa)
        

        
