# Calculadora PyQt6

Este proyecto es una calculadora gráfica desarrollada con PyQt6. La calculadora permite realizar operaciones básicas como suma, resta, multiplicación y división, y mantiene un historial de operaciones.

## Requisitos

- Python 3.x
- PyQt6

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando:
    ```bash
    pip install PyQt6
    ```

## Uso

1. Ejecuta el archivo [main.py](main.py) para iniciar la calculadora:
    ```bash
    python main.py
    ```
2. La interfaz gráfica de la calculadora se abrirá y podrás comenzar a usarla.

## Estructura del Proyecto

- [main.py](main.py): Contiene la lógica principal de la calculadora.
- [calculadora.ui](calculadora.ui): Archivo de diseño de la interfaz gráfica creado con Qt Designer.
- [calculadora.spec](calculadora.spec): Archivo de especificaciones para PyInstaller.
- [calculadora_ui.py](calculadora_ui.py): Archivo generado automáticamente por pyuic6 a partir de `calculadora.ui`.
- [icons/](icons/): Carpeta que contiene los iconos utilizados en la aplicación.
- [resources/](resources/): Carpeta que contiene recursos adicionales como capturas de pantalla y GIFs de funcionamiento.

## Funcionalidades

- **Botones Numéricos**: Permiten ingresar números del 0 al 9.
- **Operadores**: Suma, resta, multiplicación, división, porcentaje y raíz cuadrada.
- **Botón de Igual**: Calcula el resultado de la operación ingresada.
- **Botón de Borrar Último Número**: Elimina el último carácter ingresado.
- **Botón de Limpiar**: Limpia toda la pantalla de la calculadora.
- **Botón de Borrar Historial**: Borra todo el historial de operaciones.
- **Historial**: Muestra un historial de las operaciones realizadas.
- **Botón de Cerrar**: Cierra la aplicación.
- **Botón de Minimizar**: Minimiza la ventana de la aplicación.
- **Movimiento de Ventana**: Permite mover la ventana arrastrándola con el ratón.

## Capturas

![Captura de Pantalla](/resources/capture.png)
