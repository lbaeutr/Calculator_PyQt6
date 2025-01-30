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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(801, 501)
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
        self.display.setGeometry(QRect(20, 50, 411, 121))
        font1 = QFont()
        self.display.setFont(font1)
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
        self.table_history.setGeometry(QRect(450, 20, 341, 471))
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
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 150, 431, 336))
        self.layoutWidget.setStyleSheet(u"QPushButton {\n"
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
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_7 = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_7, 0, 0, 1, 1)

        self.btn_8 = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_8, 0, 1, 1, 1)

        self.btn_9 = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_9, 0, 2, 1, 1)

        self.btn_borrar_ultimo_numero = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_borrar_ultimo_numero, 0, 3, 1, 1)

        self.btn_4 = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_4, 1, 0, 1, 1)

        self.btn_5 = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_5, 1, 1, 1, 1)

        self.btn_6 = QPushButton(self.layoutWidget)
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
"/* Bot\u00f3n de limpiar (Clear) */\n"
"QPushButton#btn_clear {\n"
"    background-color: #FF5722;\n"
"    color: white;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btn_6, 1, 2, 1, 1)

        self.btn_resta = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_resta, 1, 3, 1, 1)

        self.btn_1 = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_1, 2, 0, 1, 1)

        self.btn_2 = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_2, 2, 1, 1, 1)

        self.btn_3 = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_3, 2, 2, 1, 1)

        self.btn_suma = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_suma, 2, 3, 1, 1)

        self.btn_coma = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_coma, 3, 0, 1, 1)

        self.btn_0 = QPushButton(self.layoutWidget)
        self.btn_0.setObjectName(u"btn_0")
        font2 = QFont()
        font2.setBold(True)
        self.btn_0.setFont(font2)
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

        self.gridLayout.addWidget(self.btn_0, 3, 1, 1, 1)

        self.btn_dividir = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_dividir, 3, 2, 1, 1)

        self.btn_multiplicacion = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_multiplicacion, 3, 3, 1, 1)

        self.btn_clear = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_clear, 4, 0, 1, 2)

        self.btn_igual = QPushButton(self.layoutWidget)
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

        self.gridLayout.addWidget(self.btn_igual, 4, 2, 1, 2)

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
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btn_igual.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

