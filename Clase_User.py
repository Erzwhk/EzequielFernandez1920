#Clase Usuario, metodos: datos(Imprimir bonito) y string(acomodar en base datos)
class Usuario():

    def __init__(self, username, nombre, edad , genero):
        self.username = username
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def datos(self):
        return print("Su username es: {}, nombre completo: {}, edad: {} años y de genero: {}".format(self.username,self.nombre,self.edad,self.genero))

    def string(self):
        return self.username + "," + self.nombre + "," + str(self.edad) + "," + self.genero

class Buque():

    def __init__(self, largo):
        self.largo = largo

class Buque3(Buque):

    def __init__(self,largo):
        Buque.__init__(self,largo)

    def catalogar(self):
        return print("Esto es un buque de {} posiciones, tiene la capacidad de Aterrizar helicópteros en él para el transporte de tropas".format(self.largo))

    def __repr__(self):#Camuflar objeto en el tablero
        return "O"
        
class Buque2(Buque):

    def __init__(self,largo):
        Buque.__init__(self,largo)

    def catalogar(self):
        return print("Esto es un buque de {} posiciones, tiene la capacidad de comunicarse con tierra y los otros miembros de la flota".format(self.largo))

    def __repr__(self):#Camuflear objeto en el tablero
        return "O"

class Submarino(Buque):

    def __init__(self,largo):
        Buque.__init__(self,largo)

    def catalogar(self):
        return print("Esto es un submarino de {} posicion, tiene la capacidad de poder sumergirse y emerger del agua".format(self.largo))

    def __repr__(self):#Camuflear objeto en el tablero
        return "O"
