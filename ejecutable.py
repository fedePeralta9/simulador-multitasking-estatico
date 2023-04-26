# -*- coding: utf-8 -*-
class Ejecutable():
    def __init__(self):
        self.listInstructions = []
        self.lookupTable = {}
        self.entryPoint = 0
        self.listSourceCode = []
    
    def mostrarInstrucciones(self):
        for instruccion in self.listInstructions:
            instruccion.mostrar()
    
    def mostrarResultados(self):
        print (self.listSourceCode)
        print (self.entryPoint)
        print (self.lookupTable)
        self.mostrarInstrucciones()
        
    
