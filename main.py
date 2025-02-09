import sys
import re #! Importacion para remplazos avanzados
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt 
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer
from math import factorial, cos, radians,sin


class pantalla(QMainWindow):
    def __init__(self):
        super(pantalla, self).__init__()
        uic.loadUi("calculadora.ui", self)

        #! Icono de la aplicacion
        self.setWindowIcon(QIcon("icons\IconoPPal\ios\AppIcon~ios-marketing.png"))

        #!nombre de la applicacion en ventana "Que no se vera debido a que no hay barra de titulo"
        self.setWindowTitle("Calculadora")

        self.id_operacion = 1  # Contador para el historial
        self.display.setText("0")  # Inicializar el display en 0

        # Establecer el límite de longitud del display
        self.display.setMaxLength(23)  # Limitar a 23 caracteres


        #Variables para mover la ventana con el ratón 
        # Esto permite quitar la barra de título
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint) 
        self.old_pos = None  # Guarda la posición previa del mouse

        # Conectar los botones con las funciones
        self.setup_buttons()

      
        
    def setup_buttons(self):
        # Botones numéricos
        for i in range(10):
            getattr(self, f"btn_{i}").clicked.connect(lambda _, num=i: self.add_to_display(str(num)))

        #! Botones de operadores
        self.btn_suma.clicked.connect(lambda: self.add_to_display("+"))
        self.btn_resta.clicked.connect(lambda: self.add_to_display("-"))
        self.btn_multiplicacion.clicked.connect(lambda: self.add_to_display("*"))
        self.btn_dividir.clicked.connect(lambda: self.add_to_display("/"))
        self.btn_coma.clicked.connect(lambda: self.add_to_display("."))
        #! Botones de operaciones
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
        if text == "-" and current == "0":
            self.display.setText("-")

        if current == "0":
            self.display.setText(text)
        else:   
            self.display.setText(current + text)

     

    def clear_display(self):
        self.display.setText("0")

    def delete_last_character(self):
        current = self.display.text()
        if len(current) == 1:
            self.display.setText("0")
        else:
            self.display.setText(current[:-1])


    def calculate(self):
        try:
            operation = self.display.text()  # Obtener la operación ingresada

            #! Remplazar los símbolos matemáticos por los que Python entiende y puede calcular. --> Operaciones : √, %, ^, !
            operation = operation.replace("√", "**(1/2)").replace("%", "/100").replace("^", "**")

            #! Calcular el FACTORIAL --> Esto lo que hace es buscar un número seguido de un signo de exclamación y calcula el factorial de ese número con la librería math.
            operation = re.sub(r'(\d+)!', lambda m: str(factorial(int(m.group(1)))), operation)

            #! Calcular el COSENO --> Esto lo que hace es buscar el coseno de un número en grados y lo convierte a radianes para calcularlo con la librería math.
            operation = re.sub(r'cos\((-?\d+\.?\d*)\)', lambda m: str(cos(radians(float(m.group(1))))), operation)

            #! Calcular el SENO --> Esto lo que hace es buscar el seno de un número en grados y lo convierte a radianes para calcularlo con la librería math.
            operation = re.sub(r'sin\((-?\d+\.?\d*)\)', lambda m: str(sin(radians(float(m.group(1))))), operation)

            #!  Calcular el resultado de la operación --> Funciona con la función eval() que evalúa una expresión en forma de cadena y devuelve el resultado.
            result = eval(operation, {"__builtins__": None}, {})


            self.display.setText(str(result))
            self.add_to_history(operation, result)

        except ZeroDivisionError:
            self.show_error("No se puede dividir por 0")
            self.display.setText("Math Error")
            QTimer.singleShot(1000, self.clear_display)

        except Exception:
            self.show_error("Operación no válida")
            self.display.setText("Syntax Error")
            QTimer.singleShot(1000, self.clear_display)



    def add_to_history(self, operation, result):
        row_position = self.table_history.rowCount()
        self.table_history.insertRow(row_position)
        self.table_history.setItem(row_position, 0, QTableWidgetItem(str(self.id_operacion)))
        self.table_history.setItem(row_position, 1, QTableWidgetItem(operation))
        #! Formatear el resultado a dos decimales
        # todo: Formatear el resultado a dos decimales Terminar o ver si hay que quitarlo.
        formatted_result = "{:.2f}".format(result).rjust(8)
        self.table_history.setItem(row_position, 2, QTableWidgetItem(str(formatted_result)))
               
        self.id_operacion += 1

    def clear_history(self):
        self.table_history.setRowCount(0)
        self.id_operacion = 1

    #! Funcion para mostrar mensajes de error
    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()
    
    #! Eventos para mover la ventana con el ratón
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()
    
    def mouseMoveEvent(self, event):
        if self.old_pos is not None:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None  # Resetea la posición cuando se suelta el botón del ratón



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dia = pantalla()
    dia.show()
    sys.exit(app.exec())