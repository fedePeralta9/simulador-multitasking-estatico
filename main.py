# -*- coding: utf-8 -*-
import re
from ensamblador import *
from ejecutable import *

def main():
    programa = Ensamblador('prog.asm')
    ejecutable = programa.procesar()
    ejecutable.mostrarResultados()

main()