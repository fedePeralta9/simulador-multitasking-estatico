class Instruccion():
    instrucciones=['ax','bx','cx','dx']
    def __init__(self,param1,param2):
        self.param1=param1
        self.param2=param2
        
    def procesar(self, procesador):
        pass

class Mov(Instruccion):
    def procesar(self, procesador):
        pass
    
#suma los valores 
class Add(Instruccion):
    def procesar(self, procesador):
        pass
class Jmp(Instruccion):
    def procesar(self, procesador):
        pass
    
#si es distinto de cero vuelve al ciclo
class Jnz(Instruccion):
    def procesar(self, procesador):
        pass
    
#compara dos valores, 0 si son iguales, caso contrario 1
class Cmp(Instruccion):
    def procesar(self, procesador):
        pass
#incrementa
class Inc(Instruccion):
    def procesar(self, procesador):
        pass
class Dec(Instruccion):
   def procesar(self, procesador):
       pass