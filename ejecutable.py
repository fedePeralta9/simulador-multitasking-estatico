# -*- coding: utf-8 -*-
class Ejecutable():
    def __init__(self, listInstructions, lookupTable, entryPoint, listSourceCode):
        self.listInstructions = listInstructions
        self.lookupTable = lookupTable
        self.entryPoint = entryPoint
        self.listSourceCode = listSourceCode
    
    def mostrarResultados(self):
            print (self.listSourceCode)
            print (self.entryPoint)
            print (self.lookupTable)
    
