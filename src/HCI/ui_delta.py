# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deltaJrDcTO.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *

import icons_rc
import favoriteicons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1228, 744)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color:rgb(20, 104, 177)\n"
"}")
        MainWindow.setIconSize(QSize(29, 24))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 32)")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slide_menu_container = QFrame(self.centralwidget)
        self.slide_menu_container.setObjectName(u"slide_menu_container")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_menu_container.sizePolicy().hasHeightForWidth())
        self.slide_menu_container.setSizePolicy(sizePolicy)
        self.slide_menu_container.setMinimumSize(QSize(0, 0))
        self.slide_menu_container.setMaximumSize(QSize(0, 16777215))
        self.slide_menu_container.setStyleSheet(u"background-color: #102A43;")
        self.slide_menu_container.setFrameShape(QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.slide_menu_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.slide_menu_container)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setMinimumSize(QSize(196, 0))
        font = QFont()
        self.slide_menu.setFont(font)
        self.slide_menu.setStyleSheet(u"background-color: #102A43;")
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.slide_menu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(8, 21, 34)")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Neon AI")
        font1.setPointSize(17)
        font1.setBold(True)
        font1.setWeight(QFont.Weight.Bold)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: #F5F5F5")

        self.horizontalLayout_8.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.delta = QPushButton(self.frame_7)
        self.delta.setObjectName(u"delta")
        icon = QIcon()
        icon.addFile(u":/iconos/iconsselect/Delta.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delta.setIcon(icon)
        self.delta.setIconSize(QSize(50, 50))

        self.horizontalLayout_8.addWidget(self.delta)


        self.verticalLayout_5.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.slide_menu)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_8)
        self.toolBox.setObjectName(u"toolBox")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(True)
        font2.setWeight(QFont.Weight.Bold)
        self.toolBox.setFont(font2)
        self.toolBox.setStyleSheet(u"QToolBox{\n"
"	text-align: left;\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;\n"
"	text-align: left;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #102A43\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 296, 525))
        self.page.setFont(font)
        self.page.setStyleSheet(u"color: #F5F5F5;\n"
"background-color: rgb(8, 21, 34)")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.ask_water_btn = QPushButton(self.frame_10)
        self.ask_water_btn.setObjectName(u"ask_water_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ask_water_btn.sizePolicy().hasHeightForWidth())
        self.ask_water_btn.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setWeight(QFont.Weight.Normal)
        self.ask_water_btn.setFont(font3)
        self.ask_water_btn.setMouseTracking(False)
        self.ask_water_btn.setLayoutDirection(Qt.LeftToRight)
        self.ask_water_btn.setStyleSheet(u"QPushButton {\n"
"    qproperty-iconSize: 60px 60px; /* Tama\u00f1o del \u00edcono */\n"
"    text-align: left;              /* Alinea el texto a la izquierda */\n"
"    padding-left: 10px;            /* Espacio entre el borde e \u00edcono */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/iconsselect/Agua.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ask_water_btn.setIcon(icon1)
        self.ask_water_btn.setIconSize(QSize(60, 60))

        self.verticalLayout_8.addWidget(self.ask_water_btn)

        self.ask_food_btn = QPushButton(self.frame_10)
        self.ask_food_btn.setObjectName(u"ask_food_btn")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(20)
        self.ask_food_btn.setFont(font4)
        self.ask_food_btn.setStyleSheet(u"QPushButton {\n"
"    qproperty-iconSize: 60px 60px; /* Tama\u00f1o del \u00edcono */\n"
"    text-align: left;              /* Alinea el texto a la izquierda */\n"
"    padding-left: 10px;            /* Espacio entre el borde e \u00edcono */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/iconsselect/Comida.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ask_food_btn.setIcon(icon2)
        self.ask_food_btn.setIconSize(QSize(60, 60))

        self.verticalLayout_8.addWidget(self.ask_food_btn)

        self.ask_toilet_btn = QPushButton(self.frame_10)
        self.ask_toilet_btn.setObjectName(u"ask_toilet_btn")
        self.ask_toilet_btn.setFont(font4)
        self.ask_toilet_btn.setStyleSheet(u"QPushButton {\n"
"    qproperty-iconSize: 60px 60px; /* Tama\u00f1o del \u00edcono */\n"
"    text-align: left;              /* Alinea el texto a la izquierda */\n"
"    padding-left: 10px;            /* Espacio entre el borde e \u00edcono */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/iconsselect/Ban\u0303o.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ask_toilet_btn.setIcon(icon3)
        self.ask_toilet_btn.setIconSize(QSize(60, 60))

        self.verticalLayout_8.addWidget(self.ask_toilet_btn)

        self.ask_assistance_btn = QPushButton(self.frame_10)
        self.ask_assistance_btn.setObjectName(u"ask_assistance_btn")
        self.ask_assistance_btn.setFont(font4)
        self.ask_assistance_btn.setStyleSheet(u"QPushButton {\n"
"    qproperty-iconSize: 60px 60px; /* Tama\u00f1o del \u00edcono */\n"
"    text-align: left;              /* Alinea el texto a la izquierda */\n"
"    padding-left: 10px;            /* Espacio entre el borde e \u00edcono */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/iconos/iconsselect/Asistencia me\u0301dica.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ask_assistance_btn.setIcon(icon4)
        self.ask_assistance_btn.setIconSize(QSize(60, 60))

        self.verticalLayout_8.addWidget(self.ask_assistance_btn)

        self.ask_company_btn = QPushButton(self.frame_10)
        self.ask_company_btn.setObjectName(u"ask_company_btn")
        self.ask_company_btn.setFont(font4)
        self.ask_company_btn.setStyleSheet(u"QPushButton {\n"
"    qproperty-iconSize: 60px 60px; /* Tama\u00f1o del \u00edcono */\n"
"    text-align: left;              /* Alinea el texto a la izquierda */\n"
"    padding-left: 10px;            /* Espacio entre el borde e \u00edcono */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/iconos/iconsselect/Compan\u0303i\u0301a.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ask_company_btn.setIcon(icon5)
        self.ask_company_btn.setIconSize(QSize(60, 60))

        self.verticalLayout_8.addWidget(self.ask_company_btn)

        self.ask_entertenaiment_btn = QPushButton(self.frame_10)
        self.ask_entertenaiment_btn.setObjectName(u"ask_entertenaiment_btn")
        self.ask_entertenaiment_btn.setFont(font4)
        self.ask_entertenaiment_btn.setStyleSheet(u"QPushButton {\n"
"    qproperty-iconSize: 50px 50px; /* Tama\u00f1o del \u00edcono */\n"
"    text-align: left;              /* Alinea el texto a la izquierda */\n"
"    padding-left: 10px;            /* Espacio entre el borde e \u00edcono */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/iconos/iconsselect/Entretenimiento.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ask_entertenaiment_btn.setIcon(icon6)
        self.ask_entertenaiment_btn.setIconSize(QSize(50, 50))

        self.verticalLayout_8.addWidget(self.ask_entertenaiment_btn)


        self.verticalLayout_7.addWidget(self.frame_10, 0, Qt.AlignTop)

        icon7 = QIcon()
        icon7.addFile(u":/icons/hugeicons/hugeicons_arrow-down-01.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon7, u"Necesidades")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 257, 525))
        self.page_2.setStyleSheet(u"color: #F5F5F5;\n"
"background-color: rgb(8, 21, 34)")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.settings_btn = QPushButton(self.frame_11)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setFont(font4)
        self.settings_btn.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/iconos/iconsselect/IcBaselineSettings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon8)
        self.settings_btn.setIconSize(QSize(50, 50))

        self.verticalLayout_10.addWidget(self.settings_btn)

        self.help_btn = QPushButton(self.frame_11)
        self.help_btn.setObjectName(u"help_btn")
        self.help_btn.setFont(font4)
        self.help_btn.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/iconos/iconsselect/IcBaselineQuestionMark.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.help_btn.setIcon(icon9)
        self.help_btn.setIconSize(QSize(50, 50))

        self.verticalLayout_10.addWidget(self.help_btn)

        self.speed_btn = QPushButton(self.frame_11)
        self.speed_btn.setObjectName(u"speed_btn")
        font5 = QFont()
        font5.setPointSize(18)
        self.speed_btn.setFont(font5)
        self.speed_btn.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/iconos/iconsselect/HugeiconsWheelchair.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.speed_btn.setIcon(icon10)
        self.speed_btn.setIconSize(QSize(50, 50))

        self.verticalLayout_10.addWidget(self.speed_btn)


        self.verticalLayout_9.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(13)
        font6.setBold(False)
        font6.setItalic(True)
        font6.setUnderline(False)
        font6.setWeight(QFont.Weight.Normal)
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)

        self.verticalLayout_9.addWidget(self.label_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.toolBox.addItem(self.page_2, icon7, u"Opciones")

        self.verticalLayout_6.addWidget(self.toolBox)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.slide_menu)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.exit_button = QPushButton(self.frame_9)
        self.exit_button.setObjectName(u"exit_button")
        font7 = QFont()
        font7.setFamily(u"Segoe Fluent Icons")
        font7.setPointSize(15)
        self.exit_button.setFont(font7)
        self.exit_button.setAutoFillBackground(False)
        self.exit_button.setStyleSheet(u"color: #F5F5F5")
        icon11 = QIcon()
        icon11.addFile(u":/iconos/iconsselect/IcBaselineExitToApp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon11)
        self.exit_button.setIconSize(QSize(46, 46))

        self.horizontalLayout_9.addWidget(self.exit_button, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.frame_9, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.slide_menu_container)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: #102A43;")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.frame_5 = QFrame(self.header_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.open_close_side_bar_btn = QPushButton(self.frame_5)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        self.open_close_side_bar_btn.setEnabled(True)
        self.open_close_side_bar_btn.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/iconos/iconsselect/IconoirMenu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon12)
        self.open_close_side_bar_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_7.addWidget(self.open_close_side_bar_btn, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_5, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"color: #F5F5F5")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(135, 0))
        font8 = QFont()
        font8.setPointSize(12)
        self.lineEdit.setFont(font8)
        self.lineEdit.setStyleSheet(u"border-bottom:3px solid rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.lineEdit, 0, Qt.AlignLeft)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon13 = QIcon()
        icon13.addFile(u":/iconos/iconsselect/IconoirSearch.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon13)
        self.pushButton_6.setIconSize(QSize(50, 50))

        self.horizontalLayout_6.addWidget(self.pushButton_6, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.user_btn = QPushButton(self.frame_2)
        self.user_btn.setObjectName(u"user_btn")
        self.user_btn.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/iconos/iconsselect/IconoirUser.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon14)
        self.user_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.user_btn)

        self.notifications_btn = QPushButton(self.frame_2)
        self.notifications_btn.setObjectName(u"notifications_btn")
        self.notifications_btn.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/iconos/iconsselect/IconoirBell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notifications_btn.setIcon(icon15)
        self.notifications_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_5.addWidget(self.notifications_btn)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.frame)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/iconos/iconsselect/IconoirArrowDownLeft.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon16)
        self.minimize_window_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/iconos/iconsselect/IconoirExpand.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon17)
        self.restore_window_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/iconos/iconsselect/IconoirXmarkCircle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon18)
        self.close_window_button.setIconSize(QSize(50, 50))

        self.horizontalLayout_4.addWidget(self.close_window_button)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy1.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy1)
        self.main_body_contents.setStyleSheet(u"background-color: #0A1A2F")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_body_contents)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.buttons_image_body = QFrame(self.main_body_contents)
        self.buttons_image_body.setObjectName(u"buttons_image_body")
        self.buttons_image_body.setFrameShape(QFrame.StyledPanel)
        self.buttons_image_body.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.buttons_image_body)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.camera_feed_label = QLabel(self.buttons_image_body)
        self.camera_feed_label.setObjectName(u"camera_feed_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.camera_feed_label.sizePolicy().hasHeightForWidth())
        self.camera_feed_label.setSizePolicy(sizePolicy3)
        self.camera_feed_label.setScaledContents(False)
        self.camera_feed_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.camera_feed_label, 0, 0, 1, 1)

        self.button_body = QFrame(self.buttons_image_body)
        self.button_body.setObjectName(u"button_body")
        sizePolicy.setHeightForWidth(self.button_body.sizePolicy().hasHeightForWidth())
        self.button_body.setSizePolicy(sizePolicy)
        self.button_body.setFrameShape(QFrame.StyledPanel)
        self.button_body.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.button_body)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.right_button = QPushButton(self.button_body)
        self.right_button.setObjectName(u"right_button")
        sizePolicy2.setHeightForWidth(self.right_button.sizePolicy().hasHeightForWidth())
        self.right_button.setSizePolicy(sizePolicy2)
        self.right_button.setCursor(QCursor(Qt.SizeHorCursor))
        self.right_button.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/iconos/iconsselect/HugeiconsCircleArrowRight02.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.right_button.setIcon(icon19)
        self.right_button.setIconSize(QSize(96, 96))

        self.gridLayout_3.addWidget(self.right_button, 4, 2, 2, 1)

        self.left_button = QPushButton(self.button_body)
        self.left_button.setObjectName(u"left_button")
        sizePolicy2.setHeightForWidth(self.left_button.sizePolicy().hasHeightForWidth())
        self.left_button.setSizePolicy(sizePolicy2)
        self.left_button.setCursor(QCursor(Qt.SizeHorCursor))
        self.left_button.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/iconos/iconsselect/HugeiconsCircleArrowLeft02.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.left_button.setIcon(icon20)
        self.left_button.setIconSize(QSize(96, 96))

        self.gridLayout_3.addWidget(self.left_button, 4, 0, 2, 1)

        self.down_button = QPushButton(self.button_body)
        self.down_button.setObjectName(u"down_button")
        sizePolicy2.setHeightForWidth(self.down_button.sizePolicy().hasHeightForWidth())
        self.down_button.setSizePolicy(sizePolicy2)
        self.down_button.setCursor(QCursor(Qt.SizeVerCursor))
        self.down_button.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/iconos/iconsselect/HugeiconsCircleArrowDown02.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.down_button.setIcon(icon21)
        self.down_button.setIconSize(QSize(96, 96))

        self.gridLayout_3.addWidget(self.down_button, 5, 1, 1, 1)

        self.up_button = QPushButton(self.button_body)
        self.up_button.setObjectName(u"up_button")
        sizePolicy2.setHeightForWidth(self.up_button.sizePolicy().hasHeightForWidth())
        self.up_button.setSizePolicy(sizePolicy2)
        font9 = QFont()
        font9.setKerning(True)
        self.up_button.setFont(font9)
        self.up_button.setCursor(QCursor(Qt.SizeVerCursor))
        self.up_button.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon22 = QIcon()
        icon22.addFile(u":/iconos/iconsselect/HugeiconsCircleArrowUp02.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.up_button.setIcon(icon22)
        self.up_button.setIconSize(QSize(96, 96))

        self.gridLayout_3.addWidget(self.up_button, 4, 1, 1, 1)

        self.stop_button = QPushButton(self.button_body)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setStyleSheet(u"QPushButton:hover {\n"
"    border: 2px solid rgb(17, 86, 150)\n"
"}")
        icon23 = QIcon()
        icon23.addFile(u":/iconos/iconsselect/IcSharpMotionPhotosPaused.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_button.setIcon(icon23)
        self.stop_button.setIconSize(QSize(96, 96))

        self.gridLayout_3.addWidget(self.stop_button, 6, 1, 1, 1)


        self.gridLayout_2.addWidget(self.button_body, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.buttons_image_body, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.main_body_contents)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"background-color: #102A43;")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.footer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(16)
        font10.setBold(False)
        font10.setItalic(True)
        font10.setUnderline(False)
        font10.setWeight(QFont.Weight.Normal)
        font10.setStrikeOut(False)
        font10.setKerning(True)
        self.label.setFont(font10)
        self.label.setStyleSheet(u"color: #F5F5F5")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.footer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.wheelchair_btn = QPushButton(self.frame_6)
        self.wheelchair_btn.setObjectName(u"wheelchair_btn")
        self.wheelchair_btn.setStyleSheet(u"")
        icon24 = QIcon()
        icon24.addFile(u":/iconos/iconsselect/Paseo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.wheelchair_btn.setIcon(icon24)
        self.wheelchair_btn.setIconSize(QSize(60, 60))

        self.verticalLayout_3.addWidget(self.wheelchair_btn, 0, Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.frame_6)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.size_grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Delta", None))
        self.delta.setText("")
        self.ask_water_btn.setText(QCoreApplication.translate("MainWindow", u"Agua", None))
        self.ask_food_btn.setText(QCoreApplication.translate("MainWindow", u"Comida", None))
        self.ask_toilet_btn.setText(QCoreApplication.translate("MainWindow", u"Ba\u00f1o", None))
        self.ask_assistance_btn.setText(QCoreApplication.translate("MainWindow", u"Asistencia", None))
        self.ask_company_btn.setText(QCoreApplication.translate("MainWindow", u"Compa\u00f1\u00eda", None))
        self.ask_entertenaiment_btn.setText(QCoreApplication.translate("MainWindow", u"Entretenimiento", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Necesidades", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
        self.help_btn.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.speed_btn.setText(QCoreApplication.translate("MainWindow", u"Velocidad lenta", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"La tecnolog\u00eda no tiene l\u00edmites, las personas tampoco deber\u00edan.", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Opciones", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.open_close_side_bar_btn.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.pushButton_6.setText("")
        self.user_btn.setText("")
        self.notifications_btn.setText("")
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.camera_feed_label.setText("")
        self.right_button.setText("")
        self.left_button.setText("")
        self.down_button.setText("")
        self.up_button.setText("")
        self.stop_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Delta UI v 2.0", None))
        self.wheelchair_btn.setText("")
    # retranslateUi

