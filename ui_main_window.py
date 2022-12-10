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
        main_window.resize(1009, 890)
        main_window.setStyleSheet(u"background-color: rgb(115, 143, 167);")
        self.verticalLayout_11 = QWidget(main_window)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout = QVBoxLayout(self.verticalLayout_11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.verticalLayout_11)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 15, -1, 15)
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        font = QFont()
        font.setPointSize(12)
        self.btn_home.setFont(font)

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_tables = QPushButton(self.frame)
        self.btn_tables.setObjectName(u"btn_tables")
        self.btn_tables.setFont(font)

        self.horizontalLayout.addWidget(self.btn_tables)

        self.btn_cadastro = QPushButton(self.frame)
        self.btn_cadastro.setObjectName(u"btn_cadastro")
        self.btn_cadastro.setFont(font)

        self.horizontalLayout.addWidget(self.btn_cadastro)

        self.btn_sobre = QPushButton(self.frame)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setFont(font)

        self.horizontalLayout.addWidget(self.btn_sobre)

        self.btn_contatos = QPushButton(self.frame)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setFont(font)

        self.horizontalLayout.addWidget(self.btn_contatos)


        self.verticalLayout.addWidget(self.frame)

        self.Pages = QStackedWidget(self.verticalLayout_11)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setLineWidth(1)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background-color:rgb(195, 206, 218);")
        self.verticalLayout_9 = QVBoxLayout(self.page_home)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(self.page_home)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.label_2 = QLabel(self.page_home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_2.setPixmap(QPixmap(u"../../Pictures/estoque.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.label_9 = QLabel(self.page_home)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")

        self.verticalLayout_9.addWidget(self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_9.addWidget(self.label_6)

        self.label_5 = QLabel(self.page_home)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_9.addWidget(self.label_5)

        self.Pages.addWidget(self.page_home)
        self.page_tables = QWidget()
        self.page_tables.setObjectName(u"page_tables")
        self.verticalLayout_2 = QVBoxLayout(self.page_tables)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.page_tables)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(195, 206, 218);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_8 = QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_file = QLineEdit(self.tab)
        self.txt_file.setObjectName(u"txt_file")

        self.horizontalLayout_2.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.tab)
        self.btn_open.setObjectName(u"btn_open")

        self.horizontalLayout_2.addWidget(self.btn_open)


        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.tw_estoque = QTreeWidget(self.tab)
        self.tw_estoque.setObjectName(u"tw_estoque")

        self.verticalLayout_5.addWidget(self.tw_estoque)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.tw_saida = QTreeWidget(self.tab)
        self.tw_saida.setObjectName(u"tw_saida")

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

        self.verticalLayout_3.addWidget(self.btn_entrada)

        self.btn_saida = QPushButton(self.frame_2)
        self.btn_saida.setObjectName(u"btn_saida")

        self.verticalLayout_3.addWidget(self.btn_saida)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.Pages.addWidget(self.page_tables)
        self.page_cadastro = QWidget()
        self.page_cadastro.setObjectName(u"page_cadastro")
        self.page_cadastro.setStyleSheet(u"background-color: rgb(115, 143, 167);")
        self.verticalLayout_10 = QVBoxLayout(self.page_cadastro)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.page_cadastro)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_12 = QLabel(self.page_cadastro)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_9.addWidget(self.label_12)

        self.txt_nome = QLineEdit(self.page_cadastro)
        self.txt_nome.setObjectName(u"txt_nome")

        self.horizontalLayout_9.addWidget(self.txt_nome)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_13 = QLabel(self.page_cadastro)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_8.addWidget(self.label_13)

        self.txt_usuario = QLineEdit(self.page_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")

        self.horizontalLayout_8.addWidget(self.txt_usuario)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.page_cadastro)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_7.addWidget(self.label_14)

        self.txt_senha = QLineEdit(self.page_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_7.addWidget(self.txt_senha)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_15 = QLabel(self.page_cadastro)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_6.addWidget(self.label_15)

        self.txt_senha2 = QLineEdit(self.page_cadastro)
        self.txt_senha2.setObjectName(u"txt_senha2")
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

        self.horizontalLayout_10.addWidget(self.combobox_perfil)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_17 = QLabel(self.page_cadastro)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)

        self.btn_cadsatrar_usuario = QPushButton(self.page_cadastro)
        self.btn_cadsatrar_usuario.setObjectName(u"btn_cadsatrar_usuario")

        self.horizontalLayout_11.addWidget(self.btn_cadsatrar_usuario)

        self.label_18 = QLabel(self.page_cadastro)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_11.addWidget(self.label_18)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.Pages.addWidget(self.page_cadastro)
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.label_7 = QLabel(self.page_sobre)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(290, 120, 521, 211))
        self.Pages.addWidget(self.page_sobre)
        self.page_contato = QWidget()
        self.page_contato.setObjectName(u"page_contato")
        self.label_8 = QLabel(self.page_contato)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(280, 150, 521, 211))
        self.Pages.addWidget(self.page_contato)

        self.verticalLayout.addWidget(self.Pages)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 10, -1, 10)
        self.label_20 = QLabel(self.verticalLayout_11)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_12.addWidget(self.label_20)

        self.btn_main_cadastrar_usuario = QPushButton(self.verticalLayout_11)
        self.btn_main_cadastrar_usuario.setObjectName(u"btn_main_cadastrar_usuario")

        self.horizontalLayout_12.addWidget(self.btn_main_cadastrar_usuario)

        self.label_19 = QLabel(self.verticalLayout_11)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_12.addWidget(self.label_19)


        self.verticalLayout.addLayout(self.horizontalLayout_12)

        main_window.setCentralWidget(self.verticalLayout_11)

        self.retranslateUi(main_window)

        self.Pages.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("main_window", u"HOME", None))
        self.btn_tables.setText(QCoreApplication.translate("main_window", u"TABLES", None))
        self.btn_cadastro.setText(QCoreApplication.translate("main_window", u"CADASTRO", None))
        self.btn_sobre.setText(QCoreApplication.translate("main_window", u"SOBRE", None))
        self.btn_contatos.setText(QCoreApplication.translate("main_window", u"CONTATOS", None))
        self.label_10.setText("")
        self.label_2.setText("")
        self.label_9.setText("")
        self.label.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; color:#071330;\">Sistema de</span></p><p align=\"center\"><span style=\" font-size:48pt; color:#071330;\">controle de estoque</span></p></body></html>", None))
        self.label_6.setText("")
        self.label_5.setText("")
        self.btn_open.setText(QCoreApplication.translate("main_window", u"Abrir", None))
        self.label_4.setText(QCoreApplication.translate("main_window", u"Estoque", None))
        ___qtreewidgetitem = self.tw_estoque.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("main_window", u"Valor_Total", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("main_window", u"Valor_Unidade", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("main_window", u"Quantidade", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("main_window", u"Unidade_Medida", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("main_window", u"ID_Produto", None));
        self.label_3.setText(QCoreApplication.translate("main_window", u"sa\u00edda", None))
        ___qtreewidgetitem1 = self.tw_saida.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("main_window", u"Usu\u00e1rio_A\u00e7\u00e3o", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("main_window", u"New Column", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("main_window", u"Unidade_Medida", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("main_window", u"Id_Produto", None));
        self.btn_entrada.setText(QCoreApplication.translate("main_window", u"Entrada Produto", None))
        self.btn_saida.setText(QCoreApplication.translate("main_window", u"Sa\u00edda Produto", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("main_window", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("main_window", u"Tab 2", None))
        self.label_11.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; color:#071330;\">Cadastrar Usu\u00e1rio</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("main_window", u"Nome:", None))
        self.label_13.setText(QCoreApplication.translate("main_window", u"Usu\u00e1rio:", None))
        self.label_14.setText(QCoreApplication.translate("main_window", u"Senha:", None))
        self.label_15.setText(QCoreApplication.translate("main_window", u"Senha:", None))
        self.label_16.setText(QCoreApplication.translate("main_window", u"Perfil:", None))
        self.combobox_perfil.setItemText(0, QCoreApplication.translate("main_window", u"Usu\u00e1rio", None))
        self.combobox_perfil.setItemText(1, QCoreApplication.translate("main_window", u"Administrador", None))

        self.label_17.setText("")
        self.btn_cadsatrar_usuario.setText(QCoreApplication.translate("main_window", u"Cadastrar", None))
        self.label_18.setText("")
        self.label_7.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p><span style=\" font-size:48pt;\">P\u00e1gina sobre</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("main_window", u"<html><head/><body><p><span style=\" font-size:48pt;\">P\u00e1gina contato</span></p></body></html>", None))
        self.label_20.setText("")
        self.btn_main_cadastrar_usuario.setText(QCoreApplication.translate("main_window", u"Cadastrar Usu\u00e1rio", None))
        self.label_19.setText("")
    # retranslateUi

