import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt 

class pantalla(QMainWindow):
    def __init__(self):
        super(pantalla, self).__init__()
        uic.loadUi("calculadora.ui", self)

        self.id_operacion = 1  # Contador para el historial
        self.display.setText("0")  # Inicializar el display en 0

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

        # Botones de operadores
        self.btn_suma.clicked.connect(lambda: self.add_to_display("+"))
        self.btn_resta.clicked.connect(lambda: self.add_to_display("-"))
        self.btn_multiplicacion.clicked.connect(lambda: self.add_to_display("*"))
        self.btn_dividir.clicked.connect(lambda: self.add_to_display("/"))
        self.btn_coma.clicked.connect(lambda: self.add_to_display("."))
        self.btn_igual.clicked.connect(self.calculate)
        self.btn_borrar_ultimo_numero.clicked.connect(self.delete_last_character)
        self.btn_clear.clicked.connect(self.clear_display)
        self.btn_clear_history.clicked.connect(self.clear_history)
        #! Tenemos que añadir varios botones más que completen la rubrica
        # Botones de la ventana
        self.btn_close.clicked.connect(self.close)
        self.btn_mini.clicked.connect(self.showMinimized)


    def add_to_display(self, text):
        current = self.display.text()
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
            operation = self.display.text()
            result = eval(operation)
            self.display.setText(str(result))
            self.add_to_history(operation, result)
        except Exception as e:
            self.show_error("Operación inválida")
            self.clear_display()

    def add_to_history(self, operation, result):
        row_position = self.table_history.rowCount()
        self.table_history.insertRow(row_position)
        self.table_history.setItem(row_position, 0, QTableWidgetItem(str(self.id_operacion)))
        self.table_history.setItem(row_position, 1, QTableWidgetItem(operation))
        self.table_history.setItem(row_position, 2, QTableWidgetItem(str(result)))
           
       
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
    
    # Eventos para mover la ventana con el ratón
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.old_pos is not None:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None  # Resetea la posición cuando se suelta el b


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dia = pantalla()
    dia.show()
    sys.exit(app.exec())