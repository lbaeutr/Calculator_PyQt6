import sys
import re  
import os
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer
from math import factorial, cos, radians, sin

#! Necesario para obtener la ruta de los archivos en un ejecutable de PyInstaller
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))


class pantalla(QMainWindow):
    def __init__(self):
        super(pantalla, self).__init__()
        ui_path = os.path.join(BASE_DIR, "calculadora.ui") #! Ruta del archivo .ui para el ejecutable.
        icon_path = os.path.join(BASE_DIR, "icons/IconoPPal/ios/AppIcon~ios-marketing.png")#! Ruta del icono para el ejecutable.
        uic.loadUi(ui_path, self)

        #! Icono de la aplicación
        self.setWindowIcon(QIcon(icon_path))

        #! Nombre de la aplicación en la ventana (No visible debido a que no hay barra de título)
        self.setWindowTitle("Calculadora")

        self.id_operacion = 1  # Contador para el historial
        self.display.setText("0")  # Inicializar el display en 0
        self.result_displayed = False  # Bandera para saber si el resultado está en el display

        #! Establecer el límite de longitud del display
        self.display.setMaxLength(23)  # Limitar a 23 caracteres

        #! Variables para mover la ventana con el ratón (Quitar barra de título)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.old_pos = None  # Guarda la posición previa del mouse

        #! Configurar los botones
        self.setup_buttons()

    def setup_buttons(self):
        #! Botones numéricos
        for i in range(10):
            getattr(self, f"btn_{i}").clicked.connect(lambda _, num=i: self.add_to_display(str(num)))

        #! Botones de operadores
        self.btn_suma.clicked.connect(lambda: self.add_to_display("+"))
        self.btn_resta.clicked.connect(lambda: self.add_to_display("-"))
        self.btn_multiplicacion.clicked.connect(lambda: self.add_to_display("*"))
        self.btn_dividir.clicked.connect(lambda: self.add_to_display("/"))
        self.btn_coma.clicked.connect(lambda: self.add_to_display("."))

        #! Botones de funciones matemáticas
        self.btn_parentesis_der.clicked.connect(lambda: self.add_to_display(")"))
        self.btn_parentesis_izq.clicked.connect(lambda: self.add_to_display("("))
        self.btn_raiz.clicked.connect(lambda: self.add_to_display("√"))
        self.btn_porcentaje.clicked.connect(lambda: self.add_to_display("%"))
        self.btn_igual.clicked.connect(self.calculate)

        #! Botones de borrar
        self.btn_borrar_ultimo_numero.clicked.connect(self.delete_last_character)
        self.btn_clear.clicked.connect(self.clear_display)
        self.btn_clear_history.clicked.connect(self.clear_history)

        #! Botones de operaciones avanzadas
        self.btn_exp.clicked.connect(lambda: self.add_to_display("^"))
        self.btn_fac.clicked.connect(lambda: self.add_to_display("!"))
        self.btn_cose.clicked.connect(lambda: self.add_to_display("cos("))
        self.btn_seno.clicked.connect(lambda: self.add_to_display("sin("))

        #! Botones de la ventana
        self.btn_close.clicked.connect(self.close)
        self.btn_mini.clicked.connect(self.showMinimized)

    def add_to_display(self, text):
        current = self.display.text()

        #! ✅ Si hay un resultado y el usuario introduce un número o función matemática, resetear el display
        if self.result_displayed:
            if text.isdigit() or text == "(" or text in ["cos(", "sin("]:
                self.display.setText(text)  # Se reemplaza el display
            else:
                self.display.setText(current + text)  # Se agrega el operador
            self.result_displayed = False  # Restablecer la bandera
            return

        #! ✅ Si el usuario introduce "-", y el display es "0", mostrarlo sin concatenar con el 0
        if text == "-" and current == "0":
            self.display.setText("-")
            return

        #! ✅ Si el usuario introduce una función matemática y el display es "0", lo borra
        if current == "0" and text in ["cos(", "sin("]:
            self.display.setText(text)
            return

        #! ✅ Evitar múltiples ceros innecesarios
        if current == "0" and text.isdigit():
            self.display.setText(text)
        else:
            self.display.setText(current + text)

    #! Limpiar el display
    def clear_display(self):
        self.display.setText("0")

    #! Borrar el último caracter del display --> Funciona de la siguiente manera: Si el display tiene un solo caracter, se reemplaza por 0, de lo contrario, se elimina el último caracter
    def delete_last_character(self):
        current = self.display.text()
        if len(current) == 1:
            self.display.setText("0")
        else:
            self.display.setText(current[:-1])

    #! Para calcular la operación ingresada por el usuario
    def calculate(self):
        try:
            original_operation = self.display.text()  #! Obtener la operación ingresada
            operation = original_operation  #! Copiar la operación original para mostrarla en el historial

            #!Verificar si hay paréntesis sin cerrar --> Funciona de la siguiente manera: Si hay un paréntesis abierto sin cerrar, se lanza un error de ValueError indicando que falta un paréntesis
            if operation.count("(") != operation.count(")"):
                raise ValueError("Falta un paréntesis")

            #!Reemplazar símbolos matemáticos --> Funciona de la siguiente manera: Se reemplazan los símbolos matemáticos por los que Python puede interpretar
            operation = operation.replace("√", "**(1/2)").replace("%", "/100").replace("^", "**")

            #!Calcular el FACTORIAL --> Funciona de la siguiente manera: Se busca un número seguido de un signo de exclamación y se calcula el factorial de ese número
            operation = re.sub(r'(\d+)!', lambda m: str(factorial(int(m.group(1)))), operation)

            #!Calcular el COSENO --> Funciona de la siguiente manera: Se busca un número entre paréntesis y se calcula el coseno de ese número
            operation = re.sub(r'cos\((-?\d+\.?\d*)\)', lambda m: str(cos(radians(float(m.group(1))))), operation)

            #!Calcular el SENO --> Funciona de la siguiente manera: Se busca un número entre paréntesis y se calcula el seno de ese número
            operation = re.sub(r'sin\((-?\d+\.?\d*)\)', lambda m: str(sin(radians(float(m.group(1))))), operation)

            #!Evaluar la operación 
            result = eval(operation, {"__builtins__": None}, {})

            #!Formatear el resultado para mostrarlo en el display
            #! Si el resultado es un número entero, se muestra sin decimales, de lo contrario, se muestra con 4 decimales como máximo y se eliminan los ceros innecesarios
            formatted_result = f"{result:.4f}".rstrip("0").rstrip(".") if isinstance(result, float) else str(result)
            self.display.setText(formatted_result)

            self.add_to_history(original_operation, result)

            #! Esta bandera evita que el resultado se sobreescriba si el usuario introduce un número después de obtener un resultado
            self.result_displayed = True

        #! Manejo de excepciones
        # ZeroDivisionError --> que puede ocurrir cuado se intenta dividir por 0
        except ZeroDivisionError:
            self.show_error("No se puede dividir por 0")
            self.display.setText("Math Error")
            QTimer.singleShot(1000, self.clear_display) # Limpiar el display después de 1 segundo permitiendo que se vea el mensaje de error
        # ValueError --> que puede ocurrir cuado pasa un valor no válido, como un paréntesis sin cerrar
        except ValueError as ve:
            self.show_error(str(ve))
            self.display.setText("Error")
            QTimer.singleShot(1000, self.clear_display)
        # Excepción genérica para manejar cualquier otro error , como una operación no válida
        except Exception:
            self.show_error("Operación no válida")
            self.display.setText("Syntax Error")
            QTimer.singleShot(1000, self.clear_display)

    #! Agregar contenido al historial
    def add_to_history(self, operation, result):
        row_position = self.table_history.rowCount()
        self.table_history.insertRow(row_position)

        self.table_history.setItem(row_position, 0, QTableWidgetItem(str(self.id_operacion)))
        self.table_history.setItem(row_position, 1, QTableWidgetItem(operation))

        #!Formatear resultado para mostrarlo en la tabla
        if isinstance(result, float) and result.is_integer():
            result = int(result)  

        formatted_result = "{:.6f}".format(result) if isinstance(result, float) else str(result)
        self.table_history.setItem(row_position, 2, QTableWidgetItem(str(formatted_result)))

        #!Ajuste de tamaño de columnas consiguiendo que se ajusten al contenido --> Esto no he podido hacerlo por medio de Designer, por lo que lo hago por código
        self.table_history.resizeColumnsToContents()
        self.table_history.resizeRowsToContents()
        self.table_history.setColumnWidth(2, 100)  

        self.id_operacion += 1

    #! Limpiar el historial
    def clear_history(self):
        self.table_history.setRowCount(0)
        self.id_operacion = 1

    #! Mostrar mensaje de error
    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()
    ''' 
    La siguientes funciones permiten mover la ventana sin barra de título
    manteniendo presionado el botón izquierdo del ratón y arrastrando la ventana
    esta funcionalidad va por medios de eventos, los cuales son mousePressEvent, mouseMoveEvent y mouseReleaseEvent
    esta funcionalidad no la he implementado yo y la he tomado de stackoverflow
    '''
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.old_pos is not None:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None  


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dia = pantalla()
    dia.show()
    sys.exit(app.exec())
