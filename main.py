import sys
import re 
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer
from math import factorial, cos, radians, sin


class pantalla(QMainWindow):
    def __init__(self):
        super(pantalla, self).__init__()
        uic.loadUi("calculadora.ui", self)

        #! Icono de la aplicación
        self.setWindowIcon(QIcon("icons/IconoPPal/ios/AppIcon~ios-marketing.png"))

        #! Nombre de la aplicación en la ventana (No visible debido a que no hay barra de título)
        self.setWindowTitle("Calculadora")

        self.id_operacion = 1  # Contador para el historial
        self.display.setText("0")  # Inicializar el display en 0
        self.result_displayed = False  # Bandera para saber si el resultado está en el display 

        # Establecer el límite de longitud del display
        self.display.setMaxLength(23)  # Limitar a 23 caracteres

        # Variables para mover la ventana con el ratón (Quitar barra de título)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.old_pos = None  # Guarda la posición previa del mouse

        # Configurar los botones
        self.setup_buttons()

    def setup_buttons(self):
        # Botones numéricos, función lambda para capturar el valor de i en cada iteración del bucle for 
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

        # Si hay un resultado mostrado y el usuario introduce un número, resetear el display 
        if self.result_displayed:
            if text.isdigit() or text == "(" or text in ["cos(", "sin("]:
                self.display.setText(text)
            else:
                self.display.setText(current + text)
            self.result_displayed = False  
            return

        # Si el usuario introduce un "-", y el display es "0", mostrarlo sin concatenar con el 0
        if text == "-" and current == "0":
            self.display.setText("-")
            return

        # Si el usuario introduce una función matematica y el display es "0", lo borra
        if current == "0" and text in ["cos(", "sin("]:
            self.display.setText(text)
            return

        # Evitar multiples ceros innecesarios
        if current == "0" and text.isdigit():
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
            original_operation = self.display.text()
            operation = original_operation  # Copiar la operación original para mostrarla en el historial

            #! Reemplazar símbolos matemáticos
            operation = operation.replace("√", "**(1/2)").replace("%", "/100").replace("^", "**")

            #! Calcular el FACTORIAL
            operation = re.sub(r'(\d+)!', lambda m: str(factorial(int(m.group(1)))), operation)

            #! Calcular el COSENO
            operation = re.sub(r'cos\((-?\d+\.?\d*)\)', lambda m: str(cos(radians(float(m.group(1))))), operation)

            #! Calcular el SENO
            operation = re.sub(r'sin\((-?\d+\.?\d*)\)', lambda m: str(sin(radians(float(m.group(1))))), operation)

            #! Evaluar la operación en un entorno seguro
            result = eval(operation, {"__builtins__": None}, {})

            #! Formatear el resultado
            formatted_result = "{:.6f}".format(result) if isinstance(result, float) else str(result)
            self.display.setText(formatted_result)

            self.add_to_history(original_operation, result)

            #! Indicar que un resultado fue mostrado
            self.result_displayed = True

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

        #! Formatear resultado adecuadamente
        if isinstance(result, float) and result.is_integer():
            result = int(result)  # Convierte a numero entero sino tiene decimales!

        formatted_result = "{:.6f}".format(result) if isinstance(result, float) else str(result)
        self.table_history.setItem(row_position, 2, QTableWidgetItem(str(formatted_result)))

        #! Ajuste de tamaño de columnas
        self.table_history.resizeColumnsToContents()
        self.table_history.resizeRowsToContents()
        self.table_history.setColumnWidth(2, 100)  

        self.id_operacion += 1

    def clear_history(self):
        self.table_history.setRowCount(0)
        self.id_operacion = 1

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(message)
        msg.exec()

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
