# -*- coding: utf-8 -*-

from ensamblador import *
from ejecutable import *

def main():
    programa = Ensamblador('prog.asm')
    ejecutable = programa.procesar()
    ejecutable.mostrarResultados()
    
main()
