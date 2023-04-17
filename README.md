# simulador-multitasking-estatico
Simulación de Multitasking estático de un Sistema Operativo

1. En la primera entrega, en base a un programa en assembler se debe generar un “ejecutable”

    a. Clases a implementar: Ensamblador, Ejecutable, clases asociadas a las instrucciones assembler (sólo las definiciones)

## Arquitectura/Clases

**Ensamblador:**
* Toma el archivo fuente en assembler y genera un Ejecutable
* Si hay un error debe reportar un mensaje y la línea del error

**Ejecutable:**
* Implementa el método procesar(file_name)
* Variables de instancia:
    * entryPoint
    * Lista con las instrucciones del código fuente
    * Diccionario llamado “lookupTable” que va a contener como claves los
    labels/etiquetas del programa y como valor la dirección de ese label
        * Ejemplo (“Ciclo” => 2, “Continuar” => 6)
    * Lista de instrucciones: el i-esimo elemento va a ser la instrucción ejecutable de la i-esima instrucción del programa

**Instruccion:**
* Que tenga un descendiente por cada tipo de instruccion
* O sea las subclases serían: Mov, Add, Cmp, Inc, Dec, ect

**instrucciones**

Mov:
* Mov ax, bx
* Mov ax, 1
* Mover un valor literal o el valor de otro registro al registro de la izquierda

Add:
* Add ax, bx
* Add ax, 3
* suma dos registros o un registro y un valor literal y deja el resultado en el registro de la izquierda

Jmp:
* Jmp <label/etiqueta>
* Saltar al lugar del programa que está referenciado por la etiqueta

Jnz:
* Jnz <label/etiqueta>
* Saltar al lugar del programa que está referenciado por la etiqueta si el flag está en 1 (si no pasa a la siguiente instrucción)

Cmp:
* Cmp ax, bx
* Cmp ax, 5
* Compara por igual (=) dos registros o un registro y un valor literal y setea el flag en 0 si la comparación da verdadera si no lo setea en 1

Inc:
* Inc ax
* Incrementa en 1 el valor de un registro

Dec:
* Dec ax
* Decrementa en 1 el valor de un registro

### Ejemplo
Contexto: el parseo del archivo fuente sucede en el método procesar (nombreArchivo) de la clase Ensamblador

## Pasos:
1. Crear una instancia Ejecutable
2. Recorrer el archivo línea por línea
3. Discernir si la línea contiene una instrucción o una etiqueta

    a. Si contiene un etiqueta tenemos que agregar en el diccionario lookupTable el par <etiqueta, posición de la instrucción correspondiente>
    
    b. Si contiene una instrucción, tendremos que indicar el tipo y los parámetros para generar la instrucción correspondiente
