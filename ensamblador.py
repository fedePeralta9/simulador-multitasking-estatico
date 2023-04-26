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
    
    def esEntryPoint(self, etiqueta):
        resultado = False
        if(etiqueta.lower().replace('_','') == "entrypoint"):
            resultado = True
        return resultado
    
    def definirSaltosEtiquetas(self, listInstructions, lookupTable, errores):
        for indice, isntruction in enumerate(listInstructions):
            if ((isinstance(isntruction, Jmp) or isinstance(isntruction, Jnz)) and isinstance(isntruction.param1, str)):
                #'Fin' esta en el dic
                if(isntruction.param1 in lookupTable):
                    #indice 'Fin' : 10
                    indiceEtiqueta = lookupTable.get(isntruction.param1)
                    #Jmp('Fin') => Jmp
                    nombreClase = isntruction.__class__
                    #isntanci en el lugar de Jmp('Fin') = Jmp(10)
                    listInstructions[indice] = nombreClase(indiceEtiqueta)
                else:
                    errores.agregarError("la etiqueta " + str(isntruction.param1) + " no existe en el programa")
    
    def matchearEtiqueta(self,matchEtiqueta, ejecutable, indiceIndtruccion):
        #si es una etiqueta
        if(matchEtiqueta):
            #guarda el nombre sin los :
            etiqueta = matchEtiqueta.group(1)
            #agregamos la etiqueta al dic (ej: 'Ciclo' : 3)
            ejecutable.lookupTable.update({etiqueta: indiceIndtruccion+1})
            #agregamos a la lista de codigo fuente cualquier etiqueta
            #Es para que las listas esten alineadas con los indices
            ejecutable.listSourceCode.append(etiqueta)
            #instanciamos en la lista de instrucciones la etiqueta como Noop()
            ejecutable.listInstructions.append(Noop())
            #si es un entrypoint guarda el indice de la siguiente instruccion a ejecutarse
            if(self.esEntryPoint(etiqueta)):
                ejecutable.entryPoint = indiceIndtruccion+1
            indiceIndtruccion +=1
    
    def matchearInstruccion(self,matchInstruccionUnParametro,matchInstruccionDosParametros, linea, ejecutable,REGISTROS,indiceIndtruccion):
        if(matchInstruccionUnParametro or matchInstruccionDosParametros):
            indiceIndtruccion +=1
            self.matchearInstruccionDeDosParametros(matchInstruccionDosParametros, linea, ejecutable)
            self.matchearInstruccionDeUnParametro(matchInstruccionUnParametro,ejecutable,REGISTROS)
              
    def matchearInstruccionDeUnParametro(self,matchInstruccionUnParametro,ejecutable,REGISTROS):
        
        if(matchInstruccionUnParametro):
            #agregamos a la lista de codigo fuente la instruccion
            ejecutable.listSourceCode.append(matchInstruccionUnParametro.group().rstrip())
            #tomamos el nombre de la instruccion con global para poder instanciar la clase
            instanciaInstruccion = globals()[matchInstruccionUnParametro.group(1)]
            #si es una instruccion Inc o Dec, y su parametro esta en registros 
            self.identificarParametroCoRegistro(REGISTROS,matchInstruccionUnParametro,ejecutable,instanciaInstruccion)
            
            #si es una instruccion Jmp o Jnz, y su parametro no esta en registros ya que debe ser una etiqueta
            self.identificarParametroConEtiqueta(REGISTROS,matchInstruccionUnParametro,ejecutable,instanciaInstruccion)
    
    def matchearInstruccionDeDosParametros(self, matchInstruccionDosParametros, linea, ejecutable):
        #si es de dos
        if(matchInstruccionDosParametros):
            #tomamos el nombre de la instruccion con global para poder instanciar la clase
            instanciaInstruccion = globals()[matchInstruccionDosParametros.group(1)]
            #matcheamos los parametros y los guardamos en param1 y 2
            matchParametros = re.search('\s*(\w+),\s*(\w+)', linea)
            param1 = matchParametros.group(1)
            param2 = matchParametros.group(2)
            #agregamos a la lista de codigo fuente la instruccion (ej: 'Mov Ax, 1') 
            #la funcion rstrip() es para quitar \n al final
            ejecutable.listSourceCode.append(matchInstruccionDosParametros.group().rstrip())
            #instanciamos en la lista de instrucciones(ej: Mov(Ax,1))
            ejecutable.listInstructions.append(instanciaInstruccion(param1,param2))
        
    def identificarParametroConEtiqueta(self,REGISTROS,matchInstruccionUnParametro,ejecutable,instanciaInstruccion):
        if(matchInstruccionUnParametro.group(1) in ['Jmp','Jnz'] and not(matchInstruccionUnParametro.group(2) in REGISTROS)):
            #matcheamos el parametro
            param1 = matchInstruccionUnParametro.group(2)
            #busca la clave en el dic si existe devuelve el valor si no lo segundo
            #ej: get('Ciclo', 'Ciclo') => como existe devuelve 3
            indiceEtiqueta = ejecutable.lookupTable.get(param1, param1)
            #jmp Ciclo → existe en lookupTable {Ciclo => 3}? si → listInstruccion [Jmp(3)]
            #jmp Fin → existe en lookupTable { } ? no → listInstruccion [Jmp(‘Fin’)]

            #instanciamos en la lista de instrucciones(ej: Jmp(3))
            ejecutable.listInstructions.append(instanciaInstruccion(indiceEtiqueta))
    
    def identificarParametroCoRegistro(self,REGISTROS,matchInstruccionUnParametro,ejecutable,instanciaInstruccion):
        if(matchInstruccionUnParametro.group(1) in ['Inc','Dec'] and matchInstruccionUnParametro.group(2) in REGISTROS):
            #matcheamos el parametro
            param1 = matchInstruccionUnParametro.group(2)
            #instanciamos en la lista de instrucciones(ej: Inc(Ax))
            ejecutable.listInstructions.append(instanciaInstruccion(param1))
    
    def procesar(self):
        ejecutable = Ejecutable()
        errores = Error()
        REGISTROS = ["ax", "bx", "cx", "dx"]
        file=open(self.archivo,'r')
        numeroLineas=1
        indiceIndtruccion=0
        for linea in file: 
            #verifica  si es una etiqueta, la agrega al dic, en listas como noop para alinear indices
            espacios = re.search('^\s*\n',linea)
            matchEtiqueta = re.search('^(\w+):', linea)
            matchInstruccionUnParametro = re.search('(Jmp|Jnz|Inc|Dec)\s+(Ax|Bx|Cx|Dx|\w+)\s*\n', linea)
            matchInstruccionDosParametros = re.search('(Mov|Add|Cmp)\s+(Ax|Bx|Cx|Dx),\s+(|Ax|Bx|Cx|Dx|\d+)\s*\n', linea)
            
            if(matchEtiqueta):
                self.matchearEtiqueta(matchEtiqueta, ejecutable, indiceIndtruccion)
            elif(matchInstruccionUnParametro or matchInstruccionDosParametros):
                self.matchearInstruccion(matchInstruccionUnParametro,matchInstruccionDosParametros, linea, ejecutable,REGISTROS,indiceIndtruccion)
            elif(espacios):
                print("es linea vacia en la linea: " +str(numeroLineas))
            else:
                errores.agregarError("Error de escritura en la Linea: "+str(numeroLineas))
            numeroLineas += 1
        file.close()
        self.definirSaltosEtiquetas(ejecutable.listInstructions, ejecutable.lookupTable, errores)
        errores.mostrarErrores()
        return ejecutable
    