# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainScreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(1010, 916)
        main_window.setStyleSheet(u"background-color:rgb(30, 65, 94);\n"
"")
        self.verticalLayout_11 = QWidget(main_window)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout = QVBoxLayout(self.verticalLayout_11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.verticalLayout_11)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(59, 126, 182);\n"
"border-radius:12px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(60, 1, 60, 1)
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setFamily(u"Source Sans Pro Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"    color: #fff;\n"
"	font-size: 20px;\n"
"	border-radius: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"    background-color: #2d618c;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setMinimumSize(QSize(0, 70))
        self.btn_tables.setFont(font)
        self.btn_tables.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_tables.setStyleSheet(u"QPushButton{\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"    color: #fff;\n"
"	font-size: 20px;\n"
"	border-radius: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"    background-color: #2d618c;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_importar = QPushButton(self.frame)
        self.btn_importar.setObjectName(u"btn_importar")
        self.btn_importar.setMinimumSize(QSize(0, 70))
        self.btn_importar.setFont(font)
        self.btn_importar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_importar.setStyleSheet(u"QPushButton{\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"    color: #fff;\n"
"	font-size: 20px;\n"
"	border-radius: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"    background-color: #2d618c;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_importar)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 70))
        font1 = QFont()
        font1.setFamily(u"Source Sans Pro Semibold")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.btn_sobre.setFont(font1)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton{\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"    color: #fff;\n"
"	font-size: 20px;\n"
"	border-radius: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"    background-color: #2d618c;\n"
"}")
        self.btn_sobre.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contatos = QPushButton(self.frame)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(0, 70))
        self.btn_contatos.setFont(font)
        self.btn_contatos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contatos.setStyleSheet(u"QPushButton{\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"    color: #fff;\n"
"	font-size: 20px;\n"
"	border-radius: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"    background-color: #2d618c;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_contatos)


        self.verticalLayout.addWidget(self.frame)

        self.Pages = QStackedWidget(self.verticalLayout_11)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color:rgb(30, 65, 94);")
        self.Pages.setLineWidth(1)
        self.page_import = QWidget()
        self.page_import.setObjectName(u"page_import")
        self.verticalLayout_16 = QVBoxLayout(self.page_import)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_19 = QLabel(self.page_import)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout_12.addWidget(self.label_19)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.txt_file = QLineEdit(self.page_import)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setMinimumSize(QSize(0, 50))
        self.txt_file.setStyleSheet(u"border: 3px solid rgb(255, 255, 255);\n"
"color: rgb(255,255,255);\n"
"border-radius: 20px 20px 0px 0px;\n"
"font-family: 'Montserrat';\n"
"font-size: 25px;\n"
"text-align: center;\n"
"")
        self.txt_file.setAlignment(Qt.AlignCenter)
        self.txt_file.setDragEnabled(False)
        self.txt_file.setReadOnly(True)
        self.txt_file.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.horizontalLayout_12.addWidget(self.txt_file)

        self.btn_open_path = QPushButton(self.page_import)
        self.btn_open_path.setObjectName(u"btn_open_path")
        self.btn_open_path.setMinimumSize(QSize(200, 50))
        self.btn_open_path.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_path.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 25px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_12.addWidget(self.btn_open_path)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_20 = QLabel(self.page_import)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_2.addWidget(self.label_20)

        self.btn_import = QPushButton(self.page_import)
        self.btn_import.setObjectName(u"btn_import")
        self.btn_import.setMinimumSize(QSize(200, 50))
        self.btn_import.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_import.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 25px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_import)

        self.label_21 = QLabel(self.page_import)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_2.addWidget(self.label_21)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)


        self.verticalLayout_14.addLayout(self.verticalLayout_12)

        self.progressBar = QProgressBar(self.page_import)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.progressBar)


        self.verticalLayout_16.addLayout(self.verticalLayout_14)

        self.Pages.addWidget(self.page_import)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background-color:rgb(30, 65, 94);")
        self.verticalLayout_17 = QVBoxLayout(self.page_home)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.page_home)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.label_2 = QLabel(self.page_home)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.label_10 = QLabel(self.page_home)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)


        self.verticalLayout_15.addLayout(self.horizontalLayout_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255)")

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_24 = QLabel(self.page_home)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_13.addWidget(self.label_24)

        self.btn_main_cadastrar_usuario = QPushButton(self.page_home)
        self.btn_main_cadastrar_usuario.setObjectName(u"btn_main_cadastrar_usuario")
        self.btn_main_cadastrar_usuario.setMinimumSize(QSize(0, 60))
        self.btn_main_cadastrar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_main_cadastrar_usuario.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 25px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_13.addWidget(self.btn_main_cadastrar_usuario)

        self.label_23 = QLabel(self.page_home)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_13.addWidget(self.label_23)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)


        self.verticalLayout_15.addLayout(self.verticalLayout_9)


        self.verticalLayout_17.addLayout(self.verticalLayout_15)

        self.Pages.addWidget(self.page_home)
        self.page_tables = QWidget()
        self.page_tables.setObjectName(u"page_tables")
        self.verticalLayout_2 = QVBoxLayout(self.page_tables)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.page_tables)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color:rgb(30, 65, 94);\n"
"Color: rgb(0, 0, 0);\n"
"font-size: 15px;")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_8 = QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.tw_estoque = QTreeWidget(self.tab)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setStyleSheet(u"Color: rgb(0, 0, 0);\n"
"font-size: 20px;")

        self.verticalLayout_5.addWidget(self.tw_estoque)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.tw_saida = QTreeWidget(self.tab)
        self.tw_saida.setObjectName(u"tw_saida")
        self.tw_saida.setStyleSheet(u"Color: rgb(0, 0, 0);\n"
"font-size: 20px;")

        self.verticalLayout_4.addWidget(self.tw_saida)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(180, 0))
        self.frame_2.setMaximumSize(QSize(200, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(31)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 9, -1, 9)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_entrada = QPushButton(self.frame_2)
        self.btn_entrada.setObjectName(u"btn_entrada")
        self.btn_entrada.setMinimumSize(QSize(0, 40))
        self.btn_entrada.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrada.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 18px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_entrada)

        self.btn_saida = QPushButton(self.frame_2)
        self.btn_saida.setObjectName(u"btn_saida")
        self.btn_saida.setMinimumSize(QSize(0, 40))
        self.btn_saida.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_saida.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 18px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_saida)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab, "")
        self.estoque = QWidget()
        self.estoque.setObjectName(u"estoque")
        self.verticalLayout_13 = QVBoxLayout(self.estoque)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_22 = QLabel(self.estoque)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 160))

        self.verticalLayout_13.addWidget(self.label_22)

        self.lineedit_estoque = QLineEdit(self.estoque)
        self.lineedit_estoque.setObjectName(u"lineedit_estoque")
        self.lineedit_estoque.setMinimumSize(QSize(0, 35))

        self.verticalLayout_13.addWidget(self.lineedit_estoque)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btn_gerar_grafico = QPushButton(self.estoque)
        self.btn_gerar_grafico.setObjectName(u"btn_gerar_grafico")
        self.btn_gerar_grafico.setMinimumSize(QSize(0, 40))
        self.btn_gerar_grafico.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar_grafico.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_14.addWidget(self.btn_gerar_grafico)

        self.btn_gerar_excel = QPushButton(self.estoque)
        self.btn_gerar_excel.setObjectName(u"btn_gerar_excel")
        self.btn_gerar_excel.setMinimumSize(QSize(0, 40))
        self.btn_gerar_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar_excel.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_14.addWidget(self.btn_gerar_excel)


        self.verticalLayout_13.addLayout(self.horizontalLayout_14)

        self.tableView_estoque = QTableView(self.estoque)
        self.tableView_estoque.setObjectName(u"tableView_estoque")

        self.verticalLayout_13.addWidget(self.tableView_estoque)

        self.tabWidget.addTab(self.estoque, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.Pages.addWidget(self.page_tables)
        self.page_cadastro = QWidget()
        self.page_cadastro.setObjectName(u"page_cadastro")
        self.page_cadastro.setStyleSheet(u"background-color:rgb(30, 65, 94);")
        self.verticalLayout_10 = QVBoxLayout(self.page_cadastro)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.page_cadastro)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.page_cadastro)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_9.addWidget(self.label_12)

        self.txt_nome = QLineEdit(self.page_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_9.addWidget(self.txt_nome)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_13 = QLabel(self.page_cadastro)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_8.addWidget(self.label_13)

        self.txt_usuario = QLineEdit(self.page_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_8.addWidget(self.txt_usuario)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.page_cadastro)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_7.addWidget(self.label_14)

        self.txt_senha = QLineEdit(self.page_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_15 = QLabel(self.page_cadastro)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_6.addWidget(self.label_15)

        self.txt_senha2 = QLineEdit(self.page_cadastro)
        self.txt_senha2.setObjectName(u"txt_senha2")
        self.txt_senha2.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.txt_senha2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.txt_senha2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_16 = QLabel(self.page_cadastro)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_10.addWidget(self.label_16)

        self.combobox_perfil = QComboBox(self.page_cadastro)
        self.combobox_perfil.addItem("")
        self.combobox_perfil.addItem("")
        self.combobox_perfil.setObjectName(u"combobox_perfil")
        self.combobox_perfil.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_10.addWidget(self.combobox_perfil)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(self.page_cadastro)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)

        self.btn_cadsatrar_usuario = QPushButton(self.page_cadastro)
        self.btn_cadsatrar_usuario.setObjectName(u"btn_cadsatrar_usuario")
        self.btn_cadsatrar_usuario.setMinimumSize(QSize(0, 40))
        self.btn_cadsatrar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadsatrar_usuario.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 30px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_11.addWidget(self.btn_cadsatrar_usuario)

        self.label_18 = QLabel(self.page_cadastro)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_11.addWidget(self.label_18)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.Pages.addWidget(self.page_cadastro)
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.verticalLayout_19 = QVBoxLayout(self.page_sobre)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_7 = QLabel(self.page_sobre)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_16.addWidget(self.label_7)

        self.label_6 = QLabel(self.page_sobre)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAutoFillBackground(False)
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(False)

        self.horizontalLayout_16.addWidget(self.label_6)

        self.label_25 = QLabel(self.page_sobre)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_16.addWidget(self.label_25)


        self.verticalLayout_18.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_26 = QLabel(self.page_sobre)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_15.addWidget(self.label_26)

        self.label_5 = QLabel(self.page_sobre)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255)")

        self.horizontalLayout_15.addWidget(self.label_5)

        self.label_27 = QLabel(self.page_sobre)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_15.addWidget(self.label_27)


        self.verticalLayout_18.addLayout(self.horizontalLayout_15)


        self.verticalLayout_19.addLayout(self.verticalLayout_18)

        self.label_28 = QLabel(self.page_sobre)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_19.addWidget(self.label_28)

        self.Pages.addWidget(self.page_sobre)
        self.page_contato = QWidget()
        self.page_contato.setObjectName(u"page_contato")
        self.label_29 = QLabel(self.page_contato)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(100, 60, 801, 221))
        self.label_29.setAutoFillBackground(False)
        self.label_29.setTextFormat(Qt.AutoText)
        self.label_29.setAlignment(Qt.AlignCenter)
        self.label_29.setWordWrap(False)
        self.Pages.addWidget(self.page_contato)

        self.verticalLayout.addWidget(self.Pages)

        main_window.setCentralWidget(self.verticalLayout_11)

        self.retranslateUi(main_window)

        self.Pages.setCurrentIndex(5)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("main_window", u"HOME", None))
        self.btn_tables.setText(QCoreApplication.translate("main_window", u"TABLES", None))
        self.btn_importar.setText(QCoreApplication.translate("main_window", u"IMPORTAR", None))
        self.btn_sobre.setText(QCoreApplication.translate("main_window", u"SOBRE", None))
        self.btn_contatos.setText(QCoreApplication.translate("main_window", u"CONTATOS", None))
        self.label_19.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ffffff;\">IMPORTAR XML</span></p></body></html>", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("main_window", u"Selecione o XML que ser\u00e1 importado!", None))
        self.btn_open_path.setText(QCoreApplication.translate("main_window", u"Abrir", None))
        self.label_20.setText("")
        self.btn_import.setText(QCoreApplication.translate("main_window", u"IMPORTAR", None))
        self.label_21.setText("")
        self.label_9.setText("")
        self.label_2.setText(QCoreApplication.translate("main_window", u"<img src=\"file:///C:/Users/USER/Pictures/Frame 81.png\"/>", None))
        self.label_10.setText("")
        self.label.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#ffffff;\">Seu controle </span></p><p align=\"center\"><span style=\" font-size:48pt; color:#ffffff;\">de estoque inteligente</span></p></body></html>", None))
        self.label_24.setText("")
        self.btn_main_cadastrar_usuario.setText(QCoreApplication.translate("main_window", u"Cadastrar Usu\u00e1rio", None))
        self.label_23.setText("")
        self.label_4.setText(QCoreApplication.translate("main_window", u"Estoque", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(15, QCoreApplication.translate("main_window", u"Data_Saida", None));
        ___qtreewidgetitem.setText(14, QCoreApplication.translate("main_window", u"Usuario", None));
        ___qtreewidgetitem.setText(13, QCoreApplication.translate("main_window", u"Data_Importacao", None));
        ___qtreewidgetitem.setText(12, QCoreApplication.translate("main_window", u"Valor_Produto", None));
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("main_window", u"Unidade_Medida", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("main_window", u"Descricao", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("main_window", u"Quantidade", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("main_window", u"Codigo", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("main_window", u"Item_Nota", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("main_window", u"Valor_Nfe", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("main_window", u"Nome_Emitente", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("main_window", u"CNPJ_Emitente", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("main_window", u"Chave", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("main_window", u"Data_Emissao", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("main_window", u"Serie", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("main_window", u"NFe", None));
        self.label_3.setText(QCoreApplication.translate("main_window", u"sa\u00edda", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("main_window", u"Usuario_Acao", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("main_window", u"Quantidade_Produto", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("main_window", u"Unidade_Medida", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("main_window", u"Descricao_Produto", None));
        self.btn_entrada.setText(QCoreApplication.translate("main_window", u"Entrada Produto", None))
        self.btn_saida.setText(QCoreApplication.translate("main_window", u"Sa\u00edda Produto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("main_window", u"base", None))
        self.label_22.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">IMPORTAR XML</span></p></body></html>", None))
        self.btn_gerar_grafico.setText(QCoreApplication.translate("main_window", u"Gerar Gr\u00e1fico", None))
        self.btn_gerar_excel.setText(QCoreApplication.translate("main_window", u"Gerar Excel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.estoque), QCoreApplication.translate("main_window", u"estoque", None))
        self.label_11.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">CADASTRAR USU\u00c1RIO</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#ffffff;\">Nome:</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#ffffff;\">Usu\u00e1rio:</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#ffffff;\">Senha:</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#ffffff;\">Senha:</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; color:#ffffff;\">Perfil:</span></p></body></html>", None))
        self.combobox_perfil.setItemText(0, QCoreApplication.translate("main_window", u"Usu\u00e1rio", None))
        self.combobox_perfil.setItemText(1, QCoreApplication.translate("main_window", u"Administrador", None))

        self.label_17.setText("")
        self.btn_cadsatrar_usuario.setText(QCoreApplication.translate("main_window", u"Cadastrar", None))
        self.label_18.setText("")
        self.label_7.setText("")
        self.label_6.setText(QCoreApplication.translate("main_window", u"<IMG SRC=\"file:///C:/Users/USER/Pictures/SOBRE.png\">", None))
        self.label_25.setText("")
        self.label_26.setText("")
        self.label_5.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#000000;\">O </span><span style=\" font-size:48pt; color:#ffd343;\">SMART STOCK</span><span style=\" font-size:48pt; color:#000000;\"> est\u00e1</span></p><p align=\"center\"><span style=\" font-size:48pt; color:#000000;\">sempre lan\u00e7ando</span></p><p align=\"center\"><span style=\" font-size:48pt; color:#000000;\">novidades para que seu</span></p><p align=\"center\"><span style=\" font-size:48pt; color:#000000;\">neg\u00f3cio tenha uma</span></p><p align=\"center\"><span style=\" font-size:48pt; color:#000000;\">solu\u00e7\u00e3o de gest\u00e3o</span></p><p align=\"center\"><span style=\" font-size:48pt; color:#000000;\">moderna e segura!</span></p></body></html>", None))
        self.label_27.setText("")
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("main_window", u"<IMG SRC=\"file:///C:/Users/USER/Pictures/CONTATOS.png\">", None))
    # retranslateUi

