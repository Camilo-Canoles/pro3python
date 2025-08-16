class personas:
    #constructor de la clase
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido
    
    #metodo get
    @property
    def nombre(self):
        return self._nombre
    

    #metodo set
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

