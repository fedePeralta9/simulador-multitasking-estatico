# -*- coding: utf-8 -*-
import re
from instrucciones import *
from ejecutable import *
from error import *

#Toma el archivo fuente en assembler y genera un Ejecutable
#Si hay un error debe reportar un mensaje y la línea del error
class Ensamblador():
    def __init__(self, archivo):
        self.archivo = archivo

    def esEtiqueta(self, linea):
        resultado = False
        match = re.search('^([\w_]+):', linea)
        if(match):
            resultado = True
        return resultado
    
    def esInstruccion(self, linea):
        resultado = False
        match = re.search('\s*(mov|add|jmp|jnz|cmp|inc|dec)(.*)\s*', linea)
        if(match):
            resultado = True
        return resultado
    
    def esEntryPoint(self, etiqueta):
        resultado = False
        if(etiqueta.lower().replace('_','') == "entrypoint"):
            resultado = True
        return resultado
    
    def procesar(self):
        entryPoint = 0
        listSourceCode = []
        lookupTable = {}
        listInstructions = []
        errores = Error()
        REGISTROS = ("ax", "bx", "cx", "dx")
        with open(self.archivo, 'r') as archivo:
            lineas = archivo.readlines()
        numeroLineas = 0
        for linea in lineas: 
            #verifica  si es una etiqueta, la agrega al dic, en listas como noop para alinear indices
            if(self.esEtiqueta(linea)):
                match = re.search('^([\w_]+):', linea)
                etiqueta = match.group()
                lookupTable.update({etiqueta: numeroLineas})
                listSourceCode.append('noop')
                listInstructions.append(Noop())
                #si es un entrypoint guarda el indice
                if(self.esEntryPoint(etiqueta)):
                    entryPoint = numeroLineas
            #si es una instruccion, guarda en la lista de codigo fuente ('mov ax,1')
            elif(self.esInstruccion(linea)):
                match = re.search('(mov|add|jmp|jnz|cmp|inc|dec)(.*)', linea)
                instruccion = match.group()
                instanciaInstruccion = globals()[match.group(1).capitalize()]
                listSourceCode.append(instruccion)
                #si pertenece al de dos parametros, separa los parametros y guarda las instancias en la lista 
                if(match.group(1) in ["cmp", "add", "mov"]):
                    match = re.search('\s*(\w+),\s*(\w+)', linea)
                    param1 = match.group(1)
                    param2 = match.group(2)
                    if(param1 not in REGISTROS):
                        errores.agregarError("Error de sintaxis del registro en el primer parametro, linea " + str(numeroLineas+1))
                    #problema con si es un literal
                    #elif(param2 not in REGISTROS or not param2.isdigit()):
                        #errores.agregarError("Error de sintaxis del registro o literal en el segundo parametro, linea " + str(numeroLineas+1))
                    listInstructions.append(instanciaInstruccion(param1,param2))
                #si pertenece al de un parametro, guarda la instancia en la lista
                elif(match.group(1) in ["dec", "inc"]):
                    param1 = match.group(2)
                    listInstructions.append(instanciaInstruccion(param1))
                #resolucion de salto
                elif(match.group(1) in ["jnz", "jmp"]):
                    param1 = match.group(2)
                    indiceEtiqueta = lookupTable.get(param1, param1)
                    listInstructions.append(instanciaInstruccion(indiceEtiqueta))
            numeroLineas += 1
        errores.mostrarErrores()
        return Ejecutable(listInstructions, lookupTable, entryPoint, listSourceCode)
    