# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyarchinit_pdf_exp_ui.ui'
#
# Created: Tue Aug 19 15:01:10 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog_pdf_exp(object):
    def setupUi(self, Dialog_pdf_exp):
        Dialog_pdf_exp.setObjectName(_fromUtf8("Dialog_pdf_exp"))
        Dialog_pdf_exp.setWindowModality(QtCore.Qt.NonModal)
        Dialog_pdf_exp.setEnabled(True)
        Dialog_pdf_exp.resize(488, 362)
        Dialog_pdf_exp.setMinimumSize(QtCore.QSize(300, 279))
        Dialog_pdf_exp.setMaximumSize(QtCore.QSize(488, 362))
        Dialog_pdf_exp.setCursor(QtCore.Qt.PointingHandCursor)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/directoryExp.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_pdf_exp.setWindowIcon(icon)
        Dialog_pdf_exp.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.gridLayout_2 = QtGui.QGridLayout(Dialog_pdf_exp)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_open_dir = QtGui.QPushButton(Dialog_pdf_exp)
        self.pushButton_open_dir.setIcon(icon)
        self.pushButton_open_dir.setObjectName(_fromUtf8("pushButton_open_dir"))
        self.gridLayout_2.addWidget(self.pushButton_open_dir, 8, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Dialog_pdf_exp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 275))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 275))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.comboBox_sito = QtGui.QComboBox(self.tab)
        self.comboBox_sito.setEnabled(True)
        self.comboBox_sito.setMinimumSize(QtCore.QSize(450, 20))
        self.comboBox_sito.setMouseTracking(False)
        self.comboBox_sito.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_sito.setAcceptDrops(False)
        self.comboBox_sito.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.comboBox_sito.setEditable(True)
        self.comboBox_sito.setDuplicatesEnabled(False)
        self.comboBox_sito.setFrame(True)
        self.comboBox_sito.setObjectName(_fromUtf8("comboBox_sito"))
        self.comboBox_sito.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_sito, 1, 0, 1, 7)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.checkBox_site = QtGui.QCheckBox(self.tab)
        self.checkBox_site.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_site.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconSite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_site.setIcon(icon1)
        self.checkBox_site.setIconSize(QtCore.QSize(30, 30))
        self.checkBox_site.setObjectName(_fromUtf8("checkBox_site"))
        self.verticalLayout.addWidget(self.checkBox_site)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(378, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 6)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.checkBox_US = QtGui.QCheckBox(self.tab)
        self.checkBox_US.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_US.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconPAI.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_US.setIcon(icon2)
        self.checkBox_US.setIconSize(QtCore.QSize(30, 30))
        self.checkBox_US.setObjectName(_fromUtf8("checkBox_US"))
        self.verticalLayout_2.addWidget(self.checkBox_US)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(194, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.checkBox_individui = QtGui.QCheckBox(self.tab)
        self.checkBox_individui.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_individui.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconIND.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_individui.setIcon(icon3)
        self.checkBox_individui.setIconSize(QtCore.QSize(30, 30))
        self.checkBox_individui.setObjectName(_fromUtf8("checkBox_individui"))
        self.verticalLayout_3.addWidget(self.checkBox_individui)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 4, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_6.addWidget(self.label_7)
        self.checkBox_tafonomia = QtGui.QCheckBox(self.tab)
        self.checkBox_tafonomia.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_tafonomia.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconGrave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_tafonomia.setIcon(icon4)
        self.checkBox_tafonomia.setIconSize(QtCore.QSize(30, 30))
        self.checkBox_tafonomia.setTristate(False)
        self.checkBox_tafonomia.setObjectName(_fromUtf8("checkBox_tafonomia"))
        self.verticalLayout_6.addWidget(self.checkBox_tafonomia)
        self.gridLayout.addLayout(self.verticalLayout_6, 3, 5, 1, 2)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.checkBox_reperti = QtGui.QCheckBox(self.tab)
        self.checkBox_reperti.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_reperti.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/finds.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_reperti.setIcon(icon5)
        self.checkBox_reperti.setIconSize(QtCore.QSize(30, 30))
        self.checkBox_reperti.setObjectName(_fromUtf8("checkBox_reperti"))
        self.verticalLayout_4.addWidget(self.checkBox_reperti)
        self.gridLayout.addLayout(self.verticalLayout_4, 4, 0, 1, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_5.addWidget(self.label_6)
        self.checkBox_campioni = QtGui.QCheckBox(self.tab)
        self.checkBox_campioni.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_campioni.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/champion.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_campioni.setIcon(icon6)
        self.checkBox_campioni.setIconSize(QtCore.QSize(30, 30))
        self.checkBox_campioni.setTristate(False)
        self.checkBox_campioni.setObjectName(_fromUtf8("checkBox_campioni"))
        self.verticalLayout_5.addWidget(self.checkBox_campioni)
        self.gridLayout.addLayout(self.verticalLayout_5, 4, 1, 1, 2)
        spacerItem2 = QtGui.QSpacerItem(157, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 3, 1, 1)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_8.addWidget(self.label_9)
        self.checkBox_periodo = QtGui.QCheckBox(self.tab)
        self.checkBox_periodo.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_periodo.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconPER.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_periodo.setIcon(icon7)
        self.checkBox_periodo.setIconSize(QtCore.QSize(30, 30))
        self.checkBox_periodo.setObjectName(_fromUtf8("checkBox_periodo"))
        self.verticalLayout_8.addWidget(self.checkBox_periodo)
        self.gridLayout.addLayout(self.verticalLayout_8, 4, 4, 1, 2)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_7.addWidget(self.label_8)
        self.checkBox_struttura = QtGui.QCheckBox(self.tab)
        self.checkBox_struttura.setMinimumSize(QtCore.QSize(0, 35))
        self.checkBox_struttura.setAutoFillBackground(False)
        self.checkBox_struttura.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconStrutt.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_struttura.setIcon(icon8)
        self.checkBox_struttura.setIconSize(QtCore.QSize(30, 30))
        self.checkBox_struttura.setAutoRepeatInterval(100)
        self.checkBox_struttura.setTristate(False)
        self.checkBox_struttura.setObjectName(_fromUtf8("checkBox_struttura"))
        self.verticalLayout_7.addWidget(self.checkBox_struttura)
        self.gridLayout.addLayout(self.verticalLayout_7, 4, 6, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 5, 0, 1, 1)
        self.pushButton_exp_pdf = QtGui.QPushButton(Dialog_pdf_exp)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/pdf-icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_exp_pdf.setIcon(icon9)
        self.pushButton_exp_pdf.setObjectName(_fromUtf8("pushButton_exp_pdf"))
        self.gridLayout_2.addWidget(self.pushButton_exp_pdf, 7, 0, 1, 1)
        self.line = QtGui.QFrame(Dialog_pdf_exp)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 6, 0, 1, 1)

        self.retranslateUi(Dialog_pdf_exp)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_pdf_exp)

    def retranslateUi(self, Dialog_pdf_exp):
        Dialog_pdf_exp.setWindowTitle(QtGui.QApplication.translate("Dialog_pdf_exp", "Impostazioni del sistema", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_open_dir.setText(QtGui.QApplication.translate("Dialog_pdf_exp", "Apri la cartella di esportazione PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_pdf_exp", "Seleziona un sito da esportare...", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sito.setItemText(0, QtGui.QApplication.translate("Dialog_pdf_exp", "Seleziona un valore...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_pdf_exp", "Sito", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_site.setToolTip(QtGui.QApplication.translate("Dialog_pdf_exp", "Scheda US", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_pdf_exp", "Unità Stratigrafiche", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_US.setToolTip(QtGui.QApplication.translate("Dialog_pdf_exp", "Scheda US", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog_pdf_exp", "Individuo", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_individui.setToolTip(QtGui.QApplication.translate("Dialog_pdf_exp", "Individui", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog_pdf_exp", "Tafonomia", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_tafonomia.setToolTip(QtGui.QApplication.translate("Dialog_pdf_exp", "Tafonomia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog_pdf_exp", "Reperti", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_reperti.setToolTip(QtGui.QApplication.translate("Dialog_pdf_exp", "Inventario Materiali", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog_pdf_exp", "Campionature", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_campioni.setToolTip(QtGui.QApplication.translate("Dialog_pdf_exp", "Tafonomia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog_pdf_exp", "Periodizzazione", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_periodo.setToolTip(QtGui.QApplication.translate("Dialog_pdf_exp", "Periodizzazione", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog_pdf_exp", "Strutture", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_struttura.setToolTip(QtGui.QApplication.translate("Dialog_pdf_exp", "Strutture", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog_pdf_exp", "Parametri di esportazione", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_exp_pdf.setText(QtGui.QApplication.translate("Dialog_pdf_exp", "Esporta PDF", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
