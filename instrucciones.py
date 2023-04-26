# -*- coding: utf-8 -*-
#solo definimos las instrucciones, cada isntruccion tendra distinta manera de procesar
class Instruccion():  
    def __init__(self):
        pass
    
    def procesar(self, procesador):
        pass
    
    def mostrar(self):
        pass

#La instruccion Mov tiene dos parametros (dos registros o un registro y un literal)
#movera el valor o registro al primer parametro
class Mov(Instruccion):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def procesar(self, procesador):
        pass
    
    def mostrar(self):
        print("Mov=>"+self.param1+","+self.param2)
    
#La instruccion Add tiene dos parametros (dos registros o un registro y un literal)
#suma los registros o el literal y el registro y coloca el resultado al primer parametro 
class Add(Instruccion):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
        
    def procesar(self, procesador):
        pass
    
    def mostrar(self):
        print("Add=>"+self.param1+","+self.param2)
    
#etiqueta Jmp
#Salta al lugar del programa que está referenciado por la etiqueta
class Jmp(Instruccion):
    def __init__(self, param1):
        self.param1 = param1
    
    def procesar(self, procesador):
        pass
    
    def mostrar(self):
        print("Jmp=>"+str(self.param1))
        
#etiqueta Jnz
#Saltar al lugar del programa que está referenciado por la etiqueta si el flag está en 1 (si no pasa a la siguiente instrucción)
class Jnz(Instruccion):
    def __init__(self, param1):
        self.param1 = param1
        
    def procesar(self, procesador):
        pass
    
    def mostrar(self):
        print("Jnz=>"+str(self.param1))
    
#La instruccion Cmp tiene dos parametros (dos registros o un registro y un literal)
#Compara por igual (=) dos registros o un registro y un valor literal y setea el flag en 0 si la comparación da verdadera si no lo setea en 1
class Cmp(Instruccion):
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
    
    def procesar(self, procesador):
        pass

    def mostrar(self):
        print("Cmp=>"+self.param1+","+self.param2)
    
#tiene solo un parametro (registro)
# Incrementa en 1 el valor de un registro
class Inc(Instruccion):
    def __init__(self, param1):
        self.param1 = param1
        
    def procesar(self, procesador):
        pass
    
    def mostrar(self):
        print("Inc=>"+self.param1)
#tiene solo un parametro (registro)
#decrementa en 1 el valor de un registro
class Dec(Instruccion):
    def __init__(self, param1):
        self.param1 = param1
        
    def procesar(self, procesador):
       pass
    
    def mostrar(self):
        print("Dec=>"+self.param1)
class Noop(Instruccion):
    def procesar(self, procesador):
       pass
   
    def mostrar(self):
        print("soy una etiqueta")