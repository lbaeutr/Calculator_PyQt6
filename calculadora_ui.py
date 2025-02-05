# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 602))
        font = QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"    background-color: #121212;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.display = QLineEdit(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(20, 80, 411, 121))
        font1 = QFont()
        self.display.setFont(font1)
        self.display.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.display.setStyleSheet(u"QLineEdit {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    font-size: 32px;\n"
"    border: none;\n"
"    text-align: right;\n"
"}\n"
"")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.table_history = QTableWidget(self.centralwidget)
        if (self.table_history.columnCount() < 3):
            self.table_history.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_history.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_history.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_history.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_history.setObjectName(u"table_history")
        self.table_history.setEnabled(True)
        self.table_history.setGeometry(QRect(450, 40, 341, 531))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_history.sizePolicy().hasHeightForWidth())
        self.table_history.setSizePolicy(sizePolicy)
        self.table_history.setFont(font1)
        self.table_history.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.CrossCursor))
        self.table_history.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.table_history.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.table_history.setStyleSheet(u"QTableWidget {\n"
"    background-color: #121212;\n"
"    color: white;\n"
"    gridline-color: transparent;\n"
"    border: none;\n"
"    font-size: 20px;\n"
"	text-align: center;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    color: #FFA726;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #121212;  \n"
"    color: white;               \n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
"\n"
"")
        self.table_history.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_history.setAutoScroll(False)
        self.table_history.setGridStyle(Qt.PenStyle.SolidLine)
        self.table_history.setWordWrap(True)
        self.table_history.setRowCount(0)
        self.table_history.setColumnCount(3)
        self.table_history.horizontalHeader().setVisible(True)
        self.table_history.horizontalHeader().setDefaultSectionSize(114)
        self.table_history.horizontalHeader().setStretchLastSection(True)
        self.table_history.verticalHeader().setVisible(False)
        self.table_history.verticalHeader().setCascadingSectionResizes(True)
        self.btn_clear_history = QPushButton(self.centralwidget)
        self.btn_clear_history.setObjectName(u"btn_clear_history")
        self.btn_clear_history.setGeometry(QRect(720, 520, 52, 42))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_clear_history.sizePolicy().hasHeightForWidth())
        self.btn_clear_history.setSizePolicy(sizePolicy1)
        self.btn_clear_history.setMinimumSize(QSize(52, 42))
        self.btn_clear_history.setMaximumSize(QSize(42, 32))
        self.btn_clear_history.setStyleSheet(u"QPushButton#btn_clear_history {\n"
"    background-color: #FF9800;  /* Mismo color que el bot\u00f3n \"=\" */\n"
"    color: white;  /* Color del icono */\n"
"    border-radius: 5px;  /* Bordes sutilmente redondeados */\n"
"    border: 1px solid #FFB74D;  /* Borde ligeramente m\u00e1s claro */\n"
"    min-width: 50px;\n"
"    min-height: 40px;\n"
"}\n"
"\n"
"QPushButton#btn_clear_history:hover {\n"
"    background-color: #FFA726;  /* Naranja m\u00e1s claro al pasar el mouse */\n"
"}\n"
"\n"
"QPushButton#btn_clear_history:pressed {\n"
"    background-color: #D32F2F;  /* Rojo igual que \"Clear\" cuando se presiona */\n"
"    border: 1px solid #FF5252;\n"
"}\n"
"\n"
"QPushButton#btn_clear_history:disabled {\n"
"    background-color: #555555;  /* Gris oscuro cuando est\u00e1 deshabilitado */\n"
"    color: #888888;\n"
"    border: 1px solid #444444;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/papelera.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clear_history.setIcon(icon)
        self.btn_clear_history.setIconSize(QSize(16, 16))
        self.btn_clear_history.setFlat(True)
        self.btn_close = QPushButton(self.centralwidget)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(764, 10, 31, 24))
        font2 = QFont()
        font2.setWeight(QFont.ExtraBold)
        font2.setItalic(False)
        self.btn_close.setFont(font2)
        self.btn_close.setStyleSheet(u"QPushButton#btn_close {\n"
"    background-color: transparent;  /* Sin fondo */\n"
"    color: white;  /* Texto blanco por defecto */\n"
"    border: none;  /* Sin bordes */\n"
"    font-size: 18px;  /* Tama\u00f1o del texto */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_close:hover {\n"
"    color: #A0A0A0;  /* Gris claro al pasar el mouse */\n"
"}\n"
"")
        self.btn_close.setFlat(True)
        self.btn_mini = QPushButton(self.centralwidget)
        self.btn_mini.setObjectName(u"btn_mini")
        self.btn_mini.setGeometry(QRect(730, -19, 41, 51))
        self.btn_mini.setSizeIncrement(QSize(0, 4))
        font3 = QFont()
        font3.setWeight(QFont.ExtraBold)
        self.btn_mini.setFont(font3)
        self.btn_mini.setStyleSheet(u"QPushButton#btn_mini {\n"
"    background-color: transparent;  /* Sin fondo */\n"
"    color: white;  /* Texto blanco por defecto */\n"
"    border: none;  /* Sin bordes */\n"
"    font-size: 30px;  /* Tama\u00f1o del texto */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_mini:hover {\n"
"    color: #A0A0A0;  /* Gris claro al pasar el mouse */\n"
"}\n"
"")
        self.label_titulo = QLabel(self.centralwidget)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(10, 20, 141, 31))
        font4 = QFont()
        font4.setBold(True)
        self.label_titulo.setFont(font4)
        self.label_titulo.setStyleSheet(u"QLabel#label_titulo {\n"
"    font-size: 24px;  /* Tama\u00f1o del texto */\n"
"    font-weight: bold;  /* Negrita */\n"
"    color: white;  /* Color del texto */\n"
"    background-color: transparent;  /* Sin fondo */\n"
"}\n"
"")
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 180, 431, 404))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_porcentaje = QPushButton(self.widget)
        self.btn_porcentaje.setObjectName(u"btn_porcentaje")
        self.btn_porcentaje.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_porcentaje, 0, 0, 1, 1)

        self.btn_raiz = QPushButton(self.widget)
        self.btn_raiz.setObjectName(u"btn_raiz")
        self.btn_raiz.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_raiz, 0, 1, 1, 1)

        self.btn_parentesis_izq = QPushButton(self.widget)
        self.btn_parentesis_izq.setObjectName(u"btn_parentesis_izq")
        self.btn_parentesis_izq.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_parentesis_izq, 0, 2, 1, 1)

        self.btn_parentesis_der = QPushButton(self.widget)
        self.btn_parentesis_der.setObjectName(u"btn_parentesis_der")
        self.btn_parentesis_der.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_parentesis_der, 0, 3, 1, 1)

        self.btn_7 = QPushButton(self.widget)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_8 = QPushButton(self.widget)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(self.widget)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_borrar_ultimo_numero = QPushButton(self.widget)
        self.btn_borrar_ultimo_numero.setObjectName(u"btn_borrar_ultimo_numero")
        self.btn_borrar_ultimo_numero.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_borrar_ultimo_numero, 1, 3, 1, 1)

        self.btn_4 = QPushButton(self.widget)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_5 = QPushButton(self.widget)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_6 = QPushButton(self.widget)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_resta = QPushButton(self.widget)
        self.btn_resta.setObjectName(u"btn_resta")
        self.btn_resta.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_resta, 2, 3, 1, 1)

        self.btn_1 = QPushButton(self.widget)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_2 = QPushButton(self.widget)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_3 = QPushButton(self.widget)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_suma = QPushButton(self.widget)
        self.btn_suma.setObjectName(u"btn_suma")
        self.btn_suma.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_suma, 3, 3, 1, 1)

        self.btn_coma = QPushButton(self.widget)
        self.btn_coma.setObjectName(u"btn_coma")
        self.btn_coma.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_coma, 4, 0, 1, 1)

        self.btn_0 = QPushButton(self.widget)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setFont(font4)
        self.btn_0.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_dividir = QPushButton(self.widget)
        self.btn_dividir.setObjectName(u"btn_dividir")
        self.btn_dividir.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_dividir, 4, 2, 1, 1)

        self.btn_multiplicacion = QPushButton(self.widget)
        self.btn_multiplicacion.setObjectName(u"btn_multiplicacion")
        self.btn_multiplicacion.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_multiplicacion, 4, 3, 1, 1)

        self.btn_igual = QPushButton(self.widget)
        self.btn_igual.setObjectName(u"btn_igual")
        self.btn_igual.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_igual, 5, 2, 1, 2)

        self.btn_clear = QPushButton(self.widget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setStyleSheet(u"QPushButton {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    border: none;\n"
"    font-size: 24px;\n"
"    padding: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Bot\u00f3n de igual (=) */\n"
"QPushButton#btn_igual {\n"
"    background-color: #FF9800;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de eliminar (DEL) */\n"
"QPushButton#btn_del {\n"
"    background-color: #D32F2F;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_clear, 5, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.table_history.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None));
        ___qtablewidgetitem1 = self.table_history.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"C\u00e1lculo", None));
        ___qtablewidgetitem2 = self.table_history.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Resultado", None));
        self.btn_clear_history.setText("")
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.btn_mini.setText(QCoreApplication.translate("MainWindow", u"_", None))
        self.label_titulo.setText(QCoreApplication.translate("MainWindow", u"Calculadora", None))
        self.btn_porcentaje.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.btn_raiz.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.btn_parentesis_izq.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.btn_parentesis_der.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_borrar_ultimo_numero.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btn_resta.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btn_suma.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_coma.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_dividir.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.btn_multiplicacion.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.btn_igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi

