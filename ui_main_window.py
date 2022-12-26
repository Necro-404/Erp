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
        main_window.resize(1010, 932)
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

        self.btn_clientes = QPushButton(self.frame)
        self.btn_clientes.setObjectName(u"btn_clientes")
        self.btn_clientes.setMinimumSize(QSize(0, 70))
        self.btn_clientes.setFont(font)
        self.btn_clientes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clientes.setStyleSheet(u"QPushButton{\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"    color: #fff;\n"
"	font-size: 20px;\n"
"	border-radius: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"	color: #fff;\n"
"    background-color: #2d618c;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_clientes)

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
        self.page_cliente_cadastro = QWidget()
        self.page_cliente_cadastro.setObjectName(u"page_cliente_cadastro")
        self.verticalLayout_21 = QVBoxLayout(self.page_cliente_cadastro)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_6 = QFrame(self.page_cliente_cadastro)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_6)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_81 = QLabel(self.frame_6)
        self.label_81.setObjectName(u"label_81")

        self.horizontalLayout_66.addWidget(self.label_81)

        self.btn_cadsatrar_usuario_8 = QPushButton(self.frame_6)
        self.btn_cadsatrar_usuario_8.setObjectName(u"btn_cadsatrar_usuario_8")
        self.btn_cadsatrar_usuario_8.setMinimumSize(QSize(0, 40))
        self.btn_cadsatrar_usuario_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadsatrar_usuario_8.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_66.addWidget(self.btn_cadsatrar_usuario_8)

        self.btn_cadsatrar_usuario_10 = QPushButton(self.frame_6)
        self.btn_cadsatrar_usuario_10.setObjectName(u"btn_cadsatrar_usuario_10")
        self.btn_cadsatrar_usuario_10.setMinimumSize(QSize(0, 40))
        self.btn_cadsatrar_usuario_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadsatrar_usuario_10.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_66.addWidget(self.btn_cadsatrar_usuario_10)

        self.btn_cadsatrar_usuario_9 = QPushButton(self.frame_6)
        self.btn_cadsatrar_usuario_9.setObjectName(u"btn_cadsatrar_usuario_9")
        self.btn_cadsatrar_usuario_9.setMinimumSize(QSize(0, 40))
        self.btn_cadsatrar_usuario_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadsatrar_usuario_9.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_66.addWidget(self.btn_cadsatrar_usuario_9)

        self.label_82 = QLabel(self.frame_6)
        self.label_82.setObjectName(u"label_82")

        self.horizontalLayout_66.addWidget(self.label_82)


        self.verticalLayout_32.addLayout(self.horizontalLayout_66)

        self.tab_cadastro_cliente_3 = QTabWidget(self.frame_6)
        self.tab_cadastro_cliente_3.setObjectName(u"tab_cadastro_cliente_3")
        self.tab_cadastro_cliente_3.setMaximumSize(QSize(16777215, 621))
        self.tab_cadastro_cliente_3.setStyleSheet(u"QLabel{\n"
"	font-size:22pt; \n"
"	color:#ffffff;\n"
"	text-align: center;\n"
"}")
        self.tab_cliente_caractersticas_3 = QWidget()
        self.tab_cliente_caractersticas_3.setObjectName(u"tab_cliente_caractersticas_3")
        self.verticalLayout_33 = QVBoxLayout(self.tab_cliente_caractersticas_3)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_64 = QLabel(self.tab_cliente_caractersticas_3)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(200, 0))
        self.label_64.setLayoutDirection(Qt.LeftToRight)
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_64)

        self.txt_cliente_telefone_3 = QLineEdit(self.tab_cliente_caractersticas_3)
        self.txt_cliente_telefone_3.setObjectName(u"txt_cliente_telefone_3")
        self.txt_cliente_telefone_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_50.addWidget(self.txt_cliente_telefone_3)


        self.verticalLayout_33.addLayout(self.horizontalLayout_50)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_65 = QLabel(self.tab_cliente_caractersticas_3)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(200, 0))
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.label_65)

        self.txt_cliente_nome_3 = QLineEdit(self.tab_cliente_caractersticas_3)
        self.txt_cliente_nome_3.setObjectName(u"txt_cliente_nome_3")
        self.txt_cliente_nome_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_51.addWidget(self.txt_cliente_nome_3)


        self.verticalLayout_33.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_66 = QLabel(self.tab_cliente_caractersticas_3)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(200, 0))
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.label_66)

        self.txt_cliente_celular_3 = QLineEdit(self.tab_cliente_caractersticas_3)
        self.txt_cliente_celular_3.setObjectName(u"txt_cliente_celular_3")
        self.txt_cliente_celular_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.txt_cliente_celular_3.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_52.addWidget(self.txt_cliente_celular_3)


        self.verticalLayout_33.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_67 = QLabel(self.tab_cliente_caractersticas_3)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(200, 0))
        self.label_67.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.label_67)

        self.txt_cliente_email_3 = QLineEdit(self.tab_cliente_caractersticas_3)
        self.txt_cliente_email_3.setObjectName(u"txt_cliente_email_3")
        self.txt_cliente_email_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")
        self.txt_cliente_email_3.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_53.addWidget(self.txt_cliente_email_3)


        self.verticalLayout_33.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_68 = QLabel(self.tab_cliente_caractersticas_3)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(200, 0))
        self.label_68.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.label_68)

        self.combobox_cliente_sexo_3 = QComboBox(self.tab_cliente_caractersticas_3)
        self.combobox_cliente_sexo_3.addItem("")
        self.combobox_cliente_sexo_3.addItem("")
        self.combobox_cliente_sexo_3.setObjectName(u"combobox_cliente_sexo_3")
        self.combobox_cliente_sexo_3.setMinimumSize(QSize(200, 0))
        self.combobox_cliente_sexo_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_54.addWidget(self.combobox_cliente_sexo_3)


        self.verticalLayout_33.addLayout(self.horizontalLayout_54)

        self.tab_cadastro_cliente_3.addTab(self.tab_cliente_caractersticas_3, "")
        self.tab_cliente_documentos_3 = QWidget()
        self.tab_cliente_documentos_3.setObjectName(u"tab_cliente_documentos_3")
        self.verticalLayout_34 = QVBoxLayout(self.tab_cliente_documentos_3)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_69 = QLabel(self.tab_cliente_documentos_3)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(200, 0))
        self.label_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.label_69)

        self.txt_cliente_cpf_3 = QLineEdit(self.tab_cliente_documentos_3)
        self.txt_cliente_cpf_3.setObjectName(u"txt_cliente_cpf_3")
        self.txt_cliente_cpf_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_55.addWidget(self.txt_cliente_cpf_3)


        self.verticalLayout_34.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_70 = QLabel(self.tab_cliente_documentos_3)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(200, 0))
        self.label_70.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.label_70)

        self.txt_cliente_cnpj_3 = QLineEdit(self.tab_cliente_documentos_3)
        self.txt_cliente_cnpj_3.setObjectName(u"txt_cliente_cnpj_3")
        self.txt_cliente_cnpj_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_56.addWidget(self.txt_cliente_cnpj_3)


        self.verticalLayout_34.addLayout(self.horizontalLayout_56)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_71 = QLabel(self.tab_cliente_documentos_3)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(200, 0))
        self.label_71.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.label_71)

        self.txt_cliente_identidade_3 = QLineEdit(self.tab_cliente_documentos_3)
        self.txt_cliente_identidade_3.setObjectName(u"txt_cliente_identidade_3")
        self.txt_cliente_identidade_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_57.addWidget(self.txt_cliente_identidade_3)


        self.verticalLayout_34.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_72 = QLabel(self.tab_cliente_documentos_3)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(200, 0))
        self.label_72.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.label_72)

        self.txt_cliente_orgaoEmissor_3 = QLineEdit(self.tab_cliente_documentos_3)
        self.txt_cliente_orgaoEmissor_3.setObjectName(u"txt_cliente_orgaoEmissor_3")
        self.txt_cliente_orgaoEmissor_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_58.addWidget(self.txt_cliente_orgaoEmissor_3)


        self.verticalLayout_34.addLayout(self.horizontalLayout_58)

        self.tab_cadastro_cliente_3.addTab(self.tab_cliente_documentos_3, "")
        self.tab_cliente_endereco_3 = QWidget()
        self.tab_cliente_endereco_3.setObjectName(u"tab_cliente_endereco_3")
        self.verticalLayout_24 = QVBoxLayout(self.tab_cliente_endereco_3)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_75 = QLabel(self.tab_cliente_endereco_3)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(200, 0))
        self.label_75.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.label_75)

        self.txt_cliente_cep_3 = QLineEdit(self.tab_cliente_endereco_3)
        self.txt_cliente_cep_3.setObjectName(u"txt_cliente_cep_3")
        self.txt_cliente_cep_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_61.addWidget(self.txt_cliente_cep_3)


        self.verticalLayout_24.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_76 = QLabel(self.tab_cliente_endereco_3)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setMinimumSize(QSize(200, 0))
        self.label_76.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.label_76)

        self.txt_cliente_bairro_3 = QLineEdit(self.tab_cliente_endereco_3)
        self.txt_cliente_bairro_3.setObjectName(u"txt_cliente_bairro_3")
        self.txt_cliente_bairro_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_62.addWidget(self.txt_cliente_bairro_3)


        self.verticalLayout_24.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setSpacing(6)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_77 = QLabel(self.tab_cliente_endereco_3)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(200, 0))
        self.label_77.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.label_77)

        self.txt_cliente_numeroCasa_3 = QLineEdit(self.tab_cliente_endereco_3)
        self.txt_cliente_numeroCasa_3.setObjectName(u"txt_cliente_numeroCasa_3")
        self.txt_cliente_numeroCasa_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_64.addWidget(self.txt_cliente_numeroCasa_3)


        self.horizontalLayout_63.addLayout(self.horizontalLayout_64)

        self.label_78 = QLabel(self.tab_cliente_endereco_3)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMinimumSize(QSize(200, 0))
        self.label_78.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.label_78)

        self.txt_cliente_logradouro_3 = QLineEdit(self.tab_cliente_endereco_3)
        self.txt_cliente_logradouro_3.setObjectName(u"txt_cliente_logradouro_3")
        self.txt_cliente_logradouro_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_63.addWidget(self.txt_cliente_logradouro_3)


        self.verticalLayout_24.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_61b = QHBoxLayout()
        self.horizontalLayout_61b.setSpacing(25)
        self.horizontalLayout_61b.setObjectName(u"horizontalLayout_61b")
        self.label_73 = QLabel(self.tab_cliente_endereco_3)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(200, 0))
        self.label_73.setAlignment(Qt.AlignCenter)
        self.label_73.setMargin(0)

        self.horizontalLayout_61b.addWidget(self.label_73)

        self.txt_cliente_cidade_3 = QLineEdit(self.tab_cliente_endereco_3)
        self.txt_cliente_cidade_3.setObjectName(u"txt_cliente_cidade_3")
        self.txt_cliente_cidade_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_61b.addWidget(self.txt_cliente_cidade_3)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_74 = QLabel(self.tab_cliente_endereco_3)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setMinimumSize(QSize(200, 0))
        self.label_74.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.label_74)

        self.combobox_cliente_estado_3 = QComboBox(self.tab_cliente_endereco_3)
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.addItem("")
        self.combobox_cliente_estado_3.setObjectName(u"combobox_cliente_estado_3")
        self.combobox_cliente_estado_3.setMinimumSize(QSize(200, 0))
        self.combobox_cliente_estado_3.setStyleSheet(u"Color: rgb(255, 255, 255);\n"
"font-size: 20px;")

        self.horizontalLayout_60.addWidget(self.combobox_cliente_estado_3)


        self.horizontalLayout_61b.addLayout(self.horizontalLayout_60)


        self.verticalLayout_24.addLayout(self.horizontalLayout_61b)

        self.tab_cadastro_cliente_3.addTab(self.tab_cliente_endereco_3, "")

        self.verticalLayout_32.addWidget(self.tab_cadastro_cliente_3)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_79 = QLabel(self.frame_6)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout_65.addWidget(self.label_79)

        self.btn_cadsatrar_usuario_6 = QPushButton(self.frame_6)
        self.btn_cadsatrar_usuario_6.setObjectName(u"btn_cadsatrar_usuario_6")
        self.btn_cadsatrar_usuario_6.setMinimumSize(QSize(0, 40))
        self.btn_cadsatrar_usuario_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadsatrar_usuario_6.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_65.addWidget(self.btn_cadsatrar_usuario_6)

        self.btn_cadsatrar_usuario_7 = QPushButton(self.frame_6)
        self.btn_cadsatrar_usuario_7.setObjectName(u"btn_cadsatrar_usuario_7")
        self.btn_cadsatrar_usuario_7.setMinimumSize(QSize(0, 40))
        self.btn_cadsatrar_usuario_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadsatrar_usuario_7.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_65.addWidget(self.btn_cadsatrar_usuario_7)

        self.label_80 = QLabel(self.frame_6)
        self.label_80.setObjectName(u"label_80")

        self.horizontalLayout_65.addWidget(self.label_80)


        self.verticalLayout_32.addLayout(self.horizontalLayout_65)


        self.verticalLayout_21.addWidget(self.frame_6)

        self.Pages.addWidget(self.page_cliente_cadastro)
        self.page_cliente_clientes = QWidget()
        self.page_cliente_clientes.setObjectName(u"page_cliente_clientes")
        self.verticalLayout_22 = QVBoxLayout(self.page_cliente_clientes)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_5 = QFrame(self.page_cliente_clientes)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_5)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_83 = QLabel(self.frame_5)
        self.label_83.setObjectName(u"label_83")

        self.horizontalLayout_67.addWidget(self.label_83)

        self.btn_cadsatrar_usuario_11 = QPushButton(self.frame_5)
        self.btn_cadsatrar_usuario_11.setObjectName(u"btn_cadsatrar_usuario_11")
        self.btn_cadsatrar_usuario_11.setMinimumSize(QSize(0, 40))
        self.btn_cadsatrar_usuario_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadsatrar_usuario_11.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_67.addWidget(self.btn_cadsatrar_usuario_11)

        self.btn_cadsatrar_usuario_12 = QPushButton(self.frame_5)
        self.btn_cadsatrar_usuario_12.setObjectName(u"btn_cadsatrar_usuario_12")
        self.btn_cadsatrar_usuario_12.setMinimumSize(QSize(0, 40))
        self.btn_cadsatrar_usuario_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadsatrar_usuario_12.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_67.addWidget(self.btn_cadsatrar_usuario_12)

        self.btn_cadsatrar_usuario_13 = QPushButton(self.frame_5)
        self.btn_cadsatrar_usuario_13.setObjectName(u"btn_cadsatrar_usuario_13")
        self.btn_cadsatrar_usuario_13.setMinimumSize(QSize(0, 40))
        self.btn_cadsatrar_usuario_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadsatrar_usuario_13.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_67.addWidget(self.btn_cadsatrar_usuario_13)

        self.label_84 = QLabel(self.frame_5)
        self.label_84.setObjectName(u"label_84")

        self.horizontalLayout_67.addWidget(self.label_84)


        self.verticalLayout_29.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.btn_cliente_novoCliente_2 = QPushButton(self.frame_5)
        self.btn_cliente_novoCliente_2.setObjectName(u"btn_cliente_novoCliente_2")
        self.btn_cliente_novoCliente_2.setMinimumSize(QSize(300, 40))
        self.btn_cliente_novoCliente_2.setMaximumSize(QSize(396, 16777209))
        font2 = QFont()
        font2.setFamily(u"Source Sans Pro Semibold")
        font2.setBold(True)
        font2.setWeight(99)
        self.btn_cliente_novoCliente_2.setFont(font2)
        self.btn_cliente_novoCliente_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cliente_novoCliente_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.btn_cliente_novoCliente_2.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_34.addWidget(self.btn_cliente_novoCliente_2)

        self.lineedit_cliente_buscarCliente_2 = QLineEdit(self.frame_5)
        self.lineedit_cliente_buscarCliente_2.setObjectName(u"lineedit_cliente_buscarCliente_2")
        self.lineedit_cliente_buscarCliente_2.setMinimumSize(QSize(0, 35))
        self.lineedit_cliente_buscarCliente_2.setStyleSheet(u"border: 3px solid rgb(255, 255, 255);\n"
"color: rgb(255,255,255);\n"
"border-radius: 20px 20px 0px 0px;\n"
"font-family: 'Montserrat';\n"
"font-size: 25px;\n"
"text-align: center;\n"
"")
        self.lineedit_cliente_buscarCliente_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.lineedit_cliente_buscarCliente_2)


        self.verticalLayout_29.addLayout(self.horizontalLayout_34)

        self.verticalSpacer_4 = QSpacerItem(18, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_29.addItem(self.verticalSpacer_4)

        self.tableView_cliente_2 = QTableView(self.frame_5)
        self.tableView_cliente_2.setObjectName(u"tableView_cliente_2")
        self.tableView_cliente_2.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"color: rgb(0,0,0);\n"
"font-family: 'Montserrat';\n"
"font-size: 20px;\n"
"text-align: center;\n"
"background-color:rgb(59, 126, 182)\n"
"")
        self.tableView_cliente_2.setFrameShape(QFrame.NoFrame)
        self.tableView_cliente_2.setFrameShadow(QFrame.Sunken)
        self.tableView_cliente_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView_cliente_2.setAlternatingRowColors(False)

        self.verticalLayout_29.addWidget(self.tableView_cliente_2)


        self.verticalLayout_22.addWidget(self.frame_5)

        self.Pages.addWidget(self.page_cliente_clientes)
        self.page_cliente_exportar = QWidget()
        self.page_cliente_exportar.setObjectName(u"page_cliente_exportar")
        self.verticalLayout_23 = QVBoxLayout(self.page_cliente_exportar)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_85 = QLabel(self.page_cliente_exportar)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_68.addWidget(self.label_85)

        self.btn_cadsatrar_usuario_14 = QPushButton(self.page_cliente_exportar)
        self.btn_cadsatrar_usuario_14.setObjectName(u"btn_cadsatrar_usuario_14")
        self.btn_cadsatrar_usuario_14.setMinimumSize(QSize(0, 40))
        self.btn_cadsatrar_usuario_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadsatrar_usuario_14.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_68.addWidget(self.btn_cadsatrar_usuario_14)

        self.btn_cadsatrar_usuario_15 = QPushButton(self.page_cliente_exportar)
        self.btn_cadsatrar_usuario_15.setObjectName(u"btn_cadsatrar_usuario_15")
        self.btn_cadsatrar_usuario_15.setMinimumSize(QSize(0, 40))
        self.btn_cadsatrar_usuario_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadsatrar_usuario_15.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_68.addWidget(self.btn_cadsatrar_usuario_15)

        self.btn_cadsatrar_usuario_16 = QPushButton(self.page_cliente_exportar)
        self.btn_cadsatrar_usuario_16.setObjectName(u"btn_cadsatrar_usuario_16")
        self.btn_cadsatrar_usuario_16.setMinimumSize(QSize(0, 40))
        self.btn_cadsatrar_usuario_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadsatrar_usuario_16.setStyleSheet(u"QPushButton{\n"
"	background-color: #FFd343;\n"
"	font-weight: 800;\n"
"	font-size: 20px;\n"
"	text-align: center;\n"
"	border: 2px solid #000000;\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	font-family: \"Source Sans Pro Semibold\";\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(255, 233, 160);\n"
"	color: rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_68.addWidget(self.btn_cadsatrar_usuario_16)

        self.label_86 = QLabel(self.page_cliente_exportar)
        self.label_86.setObjectName(u"label_86")

        self.horizontalLayout_68.addWidget(self.label_86)


        self.verticalLayout_20.addLayout(self.horizontalLayout_68)

        self.label_30 = QLabel(self.page_cliente_exportar)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_20.addWidget(self.label_30)

        self.listView_2 = QListView(self.page_cliente_exportar)
        self.listView_2.setObjectName(u"listView_2")

        self.verticalLayout_20.addWidget(self.listView_2)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_8 = QLabel(self.page_cliente_exportar)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_17.addWidget(self.label_8)

        self.btn_cliente_exportarParaExcel_2 = QPushButton(self.page_cliente_exportar)
        self.btn_cliente_exportarParaExcel_2.setObjectName(u"btn_cliente_exportarParaExcel_2")
        self.btn_cliente_exportarParaExcel_2.setMinimumSize(QSize(0, 40))
        self.btn_cliente_exportarParaExcel_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cliente_exportarParaExcel_2.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_17.addWidget(self.btn_cliente_exportarParaExcel_2)

        self.label_31 = QLabel(self.page_cliente_exportar)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_17.addWidget(self.label_31)


        self.verticalLayout_20.addLayout(self.horizontalLayout_17)


        self.verticalLayout_23.addLayout(self.verticalLayout_20)

        self.Pages.addWidget(self.page_cliente_exportar)
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
        self.label_4.setStyleSheet(u"color: rgb(255,255,255);\n"
"font-family: 'Montserrat';\n"
"font-size: 25px;\n"
"text-align: center; \n"
"")

        self.verticalLayout_5.addWidget(self.label_4)

        self.tw_estoque = QTreeWidget(self.tab)
        self.tw_estoque.setObjectName(u"tw_estoque")
        self.tw_estoque.setStyleSheet(u"border: 3px solid rgb(255, 255, 255);\n"
"color: rgb(0,0,0);\n"
"font-family: 'Montserrat';\n"
"font-size: 20px;\n"
"text-align: center;\n"
"background-color:rgb(59, 126, 182)\n"
"")
        self.tw_estoque.setFrameShape(QFrame.NoFrame)
        self.tw_estoque.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.tw_estoque)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"\n"
"color: rgb(255,255,255);\n"
"font-family: 'Montserrat';\n"
"font-size: 25px;\n"
"text-align: center; \n"
"")

        self.verticalLayout_4.addWidget(self.label_3)

        self.tw_saida = QTreeWidget(self.tab)
        self.tw_saida.setObjectName(u"tw_saida")
        self.tw_saida.setStyleSheet(u"border: 3px solid rgb(255, 255, 255);\n"
"color: rgb(0,0,0);\n"
"font-family: 'Montserrat';\n"
"font-size: 20px;\n"
"text-align: center;\n"
"background-color:rgb(59, 126, 182)\n"
"")

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
        self.lineedit_estoque.setStyleSheet(u"border: 3px solid rgb(255, 255, 255);\n"
"color: rgb(255,255,255);\n"
"border-radius: 20px 20px 0px 0px;\n"
"font-family: 'Montserrat';\n"
"font-size: 25px;\n"
"text-align: center;\n"
"")

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
        self.tableView_estoque.setStyleSheet(u"")

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
        self.verticalLayout_28 = QVBoxLayout(self.page_contato)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_29 = QLabel(self.page_contato)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAutoFillBackground(False)
        self.label_29.setTextFormat(Qt.AutoText)
        self.label_29.setAlignment(Qt.AlignCenter)
        self.label_29.setWordWrap(False)

        self.verticalLayout_28.addWidget(self.label_29)

        self.Pages.addWidget(self.page_contato)

        self.verticalLayout.addWidget(self.Pages)

        main_window.setCentralWidget(self.verticalLayout_11)

        self.retranslateUi(main_window)

        self.Pages.setCurrentIndex(1)
        self.tab_cadastro_cliente_3.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("main_window", u"HOME", None))
        self.btn_clientes.setText(QCoreApplication.translate("main_window", u"CLIENTES", None))
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
        self.label_81.setText("")
        self.btn_cadsatrar_usuario_8.setText(QCoreApplication.translate("main_window", u"Cadastrar Clientes", None))
        self.btn_cadsatrar_usuario_10.setText(QCoreApplication.translate("main_window", u"Todos Clientes", None))
        self.btn_cadsatrar_usuario_9.setText(QCoreApplication.translate("main_window", u"Exportar Clientes", None))
        self.label_82.setText("")
        self.label_64.setText(QCoreApplication.translate("main_window", u"Telefone:", None))
        self.label_65.setText(QCoreApplication.translate("main_window", u"Nome:", None))
        self.label_66.setText(QCoreApplication.translate("main_window", u"Celular:", None))
        self.label_67.setText(QCoreApplication.translate("main_window", u"E-mail:", None))
        self.label_68.setText(QCoreApplication.translate("main_window", u"Sexo:", None))
        self.combobox_cliente_sexo_3.setItemText(0, QCoreApplication.translate("main_window", u"Masculino", None))
        self.combobox_cliente_sexo_3.setItemText(1, QCoreApplication.translate("main_window", u"Feminino", None))

        self.tab_cadastro_cliente_3.setTabText(self.tab_cadastro_cliente_3.indexOf(self.tab_cliente_caractersticas_3), QCoreApplication.translate("main_window", u"Caracter\u00edsticas", None))
        self.label_69.setText(QCoreApplication.translate("main_window", u"CPF:", None))
        self.label_70.setText(QCoreApplication.translate("main_window", u"CNPJ:", None))
        self.label_71.setText(QCoreApplication.translate("main_window", u"Identidade", None))
        self.label_72.setText(QCoreApplication.translate("main_window", u"Org\u00e3o Emissor:", None))
        self.tab_cadastro_cliente_3.setTabText(self.tab_cadastro_cliente_3.indexOf(self.tab_cliente_documentos_3), QCoreApplication.translate("main_window", u"Documentos", None))
        self.label_75.setText(QCoreApplication.translate("main_window", u"CEP:", None))
        self.label_76.setText(QCoreApplication.translate("main_window", u"Bairro:", None))
        self.label_77.setText(QCoreApplication.translate("main_window", u"N\u00famero:", None))
        self.label_78.setText(QCoreApplication.translate("main_window", u"Logradouro:", None))
        self.label_73.setText(QCoreApplication.translate("main_window", u"Cidade:", None))
        self.label_74.setText(QCoreApplication.translate("main_window", u"Estado:", None))
        self.combobox_cliente_estado_3.setItemText(0, QCoreApplication.translate("main_window", u"AC", None))
        self.combobox_cliente_estado_3.setItemText(1, QCoreApplication.translate("main_window", u"AL", None))
        self.combobox_cliente_estado_3.setItemText(2, QCoreApplication.translate("main_window", u"AP", None))
        self.combobox_cliente_estado_3.setItemText(3, QCoreApplication.translate("main_window", u"AM", None))
        self.combobox_cliente_estado_3.setItemText(4, QCoreApplication.translate("main_window", u"BA", None))
        self.combobox_cliente_estado_3.setItemText(5, QCoreApplication.translate("main_window", u"CE", None))
        self.combobox_cliente_estado_3.setItemText(6, QCoreApplication.translate("main_window", u"DF", None))
        self.combobox_cliente_estado_3.setItemText(7, QCoreApplication.translate("main_window", u"ES", None))
        self.combobox_cliente_estado_3.setItemText(8, QCoreApplication.translate("main_window", u"GO", None))
        self.combobox_cliente_estado_3.setItemText(9, QCoreApplication.translate("main_window", u"MA", None))
        self.combobox_cliente_estado_3.setItemText(10, QCoreApplication.translate("main_window", u"MT", None))
        self.combobox_cliente_estado_3.setItemText(11, QCoreApplication.translate("main_window", u"MS", None))
        self.combobox_cliente_estado_3.setItemText(12, QCoreApplication.translate("main_window", u"MG", None))
        self.combobox_cliente_estado_3.setItemText(13, QCoreApplication.translate("main_window", u"PA", None))
        self.combobox_cliente_estado_3.setItemText(14, QCoreApplication.translate("main_window", u"PB", None))
        self.combobox_cliente_estado_3.setItemText(15, QCoreApplication.translate("main_window", u"PR", None))
        self.combobox_cliente_estado_3.setItemText(16, QCoreApplication.translate("main_window", u"PE", None))
        self.combobox_cliente_estado_3.setItemText(17, QCoreApplication.translate("main_window", u"PI", None))
        self.combobox_cliente_estado_3.setItemText(18, QCoreApplication.translate("main_window", u"RJ", None))
        self.combobox_cliente_estado_3.setItemText(19, QCoreApplication.translate("main_window", u"RN", None))
        self.combobox_cliente_estado_3.setItemText(20, QCoreApplication.translate("main_window", u"RS", None))
        self.combobox_cliente_estado_3.setItemText(21, QCoreApplication.translate("main_window", u"RO", None))
        self.combobox_cliente_estado_3.setItemText(22, QCoreApplication.translate("main_window", u"RR", None))
        self.combobox_cliente_estado_3.setItemText(23, QCoreApplication.translate("main_window", u"SC", None))
        self.combobox_cliente_estado_3.setItemText(24, QCoreApplication.translate("main_window", u"SP", None))
        self.combobox_cliente_estado_3.setItemText(25, QCoreApplication.translate("main_window", u"SE", None))
        self.combobox_cliente_estado_3.setItemText(26, QCoreApplication.translate("main_window", u"TO", None))

        self.tab_cadastro_cliente_3.setTabText(self.tab_cadastro_cliente_3.indexOf(self.tab_cliente_endereco_3), QCoreApplication.translate("main_window", u"Endere\u00e7o", None))
        self.label_79.setText("")
        self.btn_cadsatrar_usuario_6.setText(QCoreApplication.translate("main_window", u"Cadastrar", None))
        self.btn_cadsatrar_usuario_7.setText(QCoreApplication.translate("main_window", u"Cancelar", None))
        self.label_80.setText("")
        self.label_83.setText("")
        self.btn_cadsatrar_usuario_11.setText(QCoreApplication.translate("main_window", u"Cadastrar Clientes", None))
        self.btn_cadsatrar_usuario_12.setText(QCoreApplication.translate("main_window", u"Todos Clientes", None))
        self.btn_cadsatrar_usuario_13.setText(QCoreApplication.translate("main_window", u"Exportar Clientes", None))
        self.label_84.setText("")
        self.btn_cliente_novoCliente_2.setText(QCoreApplication.translate("main_window", u"Novo Cliente", None))
        self.lineedit_cliente_buscarCliente_2.setPlaceholderText(QCoreApplication.translate("main_window", u"Buscar cliente", None))
        self.label_85.setText("")
        self.btn_cadsatrar_usuario_14.setText(QCoreApplication.translate("main_window", u"Cadastrar Clientes", None))
        self.btn_cadsatrar_usuario_15.setText(QCoreApplication.translate("main_window", u"Todos Clientes", None))
        self.btn_cadsatrar_usuario_16.setText(QCoreApplication.translate("main_window", u"Exportar Clientes", None))
        self.label_86.setText("")
        self.label_30.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">Quantidade de Clientes </span></p><p align=\"center\"><span style=\" font-size:28pt; color:#ffffff;\">Cadastrados:</span></p></body></html>", None))
        self.label_8.setText("")
        self.btn_cliente_exportarParaExcel_2.setText(QCoreApplication.translate("main_window", u"Exportar para Excel", None))
        self.label_31.setText("")
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
        ___qtreewidgetitem1.setText(4, QCoreApplication.translate("main_window", u"Usuario_Acao", None));
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("main_window", u"Quantidade_Produto", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("main_window", u"Unidade_Medida", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("main_window", u"Descricao_Produto", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("main_window", u"NFe", None));
        self.btn_entrada.setText(QCoreApplication.translate("main_window", u"Entrada Produto", None))
        self.btn_saida.setText(QCoreApplication.translate("main_window", u"Sa\u00edda Produto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("main_window", u"base", None))
        self.label_22.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">ESTOQUE COMPLETO</span></p></body></html>", None))
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

