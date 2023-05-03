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

¡Hola!

Este es el repositorio de mi proyecto de simulador de multitasking estático. En este proyecto, he creado un programa que permite simular la ejecución de varios procesos simultáneamente en un sistema operativo.

# Funcionalidades

* Permite definir varios procesos y sus tiempos de ejecución.
* Implementa un algoritmo de planificación de procesos para simular la ejecución de los procesos.
* Muestra el estado actual del sistema en cada paso de la simulación.
* Permite ajustar la velocidad de la simulación para facilitar el seguimiento del proceso.

# Cómo usar el programa

Para usar el simulador, siga estos pasos:

1. Descargue el repositorio en su ordenador.
2. Abra una terminal en la carpeta raíz del repositorio.
3. Ejecute el archivo _main.py_ para iniciar el programa.
4. Siga las instrucciones en pantalla para definir los procesos y ejecutar la simulación.

# Requisitos del sistema

* Python 3.x

# Contribuciones

Este es un proyecto de código abierto, por lo que son bienvenidas las contribuciones y sugerencias. Si desea contribuir al proyecto, siga estos pasos:

1. Fork este repositorio.
2. Cree una rama para su contribución.
3. Realice sus cambios en la rama y haga commits con mensajes descriptivos.
4. Envíe un pull request a la rama principal de este repositorio.

¡Gracias por su interés en mi proyecto! Si tiene alguna pregunta o comentario, no dude en abrir un issue en este repositorio.