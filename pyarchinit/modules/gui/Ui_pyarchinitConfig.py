# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_pyarchinitConfig.ui'
#
# Created: Fri Feb 20 15:12:48 2015
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog_Config(object):
    def setupUi(self, Dialog_Config):
        Dialog_Config.setObjectName(_fromUtf8("Dialog_Config"))
        Dialog_Config.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog_Config.setEnabled(True)
        Dialog_Config.resize(504, 494)
        Dialog_Config.setMinimumSize(QtCore.QSize(450, 279))
        Dialog_Config.setMaximumSize(QtCore.QSize(1000, 1000))
        Dialog_Config.setCursor(QtCore.Qt.PointingHandCursor)
        Dialog_Config.setMouseTracking(False)
        Dialog_Config.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconConn.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_Config.setWindowIcon(icon)
        Dialog_Config.setAutoFillBackground(True)
        Dialog_Config.setSizeGripEnabled(False)
        Dialog_Config.setModal(True)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog_Config)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(Dialog_Config)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setProperty(_fromUtf8("resize"), _fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.comboBox_Database = QtGui.QComboBox(self.tab)
        self.comboBox_Database.setEnabled(True)
        self.comboBox_Database.setMouseTracking(False)
        self.comboBox_Database.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_Database.setAcceptDrops(False)
        self.comboBox_Database.setEditable(True)
        self.comboBox_Database.setDuplicatesEnabled(False)
        self.comboBox_Database.setFrame(True)
        self.comboBox_Database.setObjectName(_fromUtf8("comboBox_Database"))
        self.comboBox_Database.addItem(_fromUtf8(""))
        self.comboBox_Database.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_Database, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_Host = QtGui.QLineEdit(self.tab)
        self.lineEdit_Host.setObjectName(_fromUtf8("lineEdit_Host"))
        self.gridLayout.addWidget(self.lineEdit_Host, 2, 1, 1, 2)
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit_Port = QtGui.QLineEdit(self.tab)
        self.lineEdit_Port.setObjectName(_fromUtf8("lineEdit_Port"))
        self.gridLayout.addWidget(self.lineEdit_Port, 3, 1, 1, 2)
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.lineEdit_DBname = QtGui.QLineEdit(self.tab)
        self.lineEdit_DBname.setObjectName(_fromUtf8("lineEdit_DBname"))
        self.gridLayout.addWidget(self.lineEdit_DBname, 4, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.lineEdit_User = QtGui.QLineEdit(self.tab)
        self.lineEdit_User.setObjectName(_fromUtf8("lineEdit_User"))
        self.gridLayout.addWidget(self.lineEdit_User, 5, 1, 1, 2)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.lineEdit_Password = QtGui.QLineEdit(self.tab)
        self.lineEdit_Password.setInputMask(_fromUtf8(""))
        self.lineEdit_Password.setText(_fromUtf8("\'\'"))
        self.lineEdit_Password.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_Password.setObjectName(_fromUtf8("lineEdit_Password"))
        self.gridLayout.addWidget(self.lineEdit_Password, 6, 1, 1, 2)
        self.pushButton_save = QtGui.QPushButton(self.tab)
        self.pushButton_save.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_save.setCheckable(False)
        self.pushButton_save.setAutoDefault(True)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.gridLayout.addWidget(self.pushButton_save, 11, 1, 1, 2)
        self.lineEdit_Logo_path = QtGui.QLineEdit(self.tab)
        self.lineEdit_Logo_path.setObjectName(_fromUtf8("lineEdit_Logo_path"))
        self.gridLayout.addWidget(self.lineEdit_Logo_path, 9, 1, 1, 2)
        self.label_16 = QtGui.QLabel(self.tab)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 9, 0, 1, 1)
        self.lineEdit_Thumb_path = QtGui.QLineEdit(self.tab)
        self.lineEdit_Thumb_path.setObjectName(_fromUtf8("lineEdit_Thumb_path"))
        self.gridLayout.addWidget(self.lineEdit_Thumb_path, 7, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.comboBox_experimental = QtGui.QComboBox(self.tab)
        self.comboBox_experimental.setEnabled(True)
        self.comboBox_experimental.setMaximumSize(QtCore.QSize(60, 16777215))
        self.comboBox_experimental.setMouseTracking(False)
        self.comboBox_experimental.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox_experimental.setAcceptDrops(False)
        self.comboBox_experimental.setEditable(True)
        self.comboBox_experimental.setDuplicatesEnabled(False)
        self.comboBox_experimental.setFrame(True)
        self.comboBox_experimental.setObjectName(_fromUtf8("comboBox_experimental"))
        self.comboBox_experimental.addItem(_fromUtf8(""))
        self.comboBox_experimental.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox_experimental, 0, 1, 1, 1)
        self.label_26 = QtGui.QLabel(self.tab)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.gridLayout.addWidget(self.label_26, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_dbname = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_dbname.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_dbname.setDragEnabled(False)
        self.lineEdit_dbname.setReadOnly(False)
        self.lineEdit_dbname.setObjectName(_fromUtf8("lineEdit_dbname"))
        self.gridLayout_3.addWidget(self.lineEdit_dbname, 1, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.tab_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)
        self.pushButton_crea_database = QtGui.QPushButton(self.tab_2)
        self.pushButton_crea_database.setEnabled(True)
        self.pushButton_crea_database.setObjectName(_fromUtf8("pushButton_crea_database"))
        self.gridLayout_3.addWidget(self.pushButton_crea_database, 1, 2, 2, 1)
        self.lineEdit_template_postgis = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_template_postgis.setObjectName(_fromUtf8("lineEdit_template_postgis"))
        self.gridLayout_3.addWidget(self.lineEdit_template_postgis, 2, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.tab_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_3.addWidget(self.label_13, 2, 1, 1, 1)
        self.lineEdit_port_db = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_port_db.setObjectName(_fromUtf8("lineEdit_port_db"))
        self.gridLayout_3.addWidget(self.lineEdit_port_db, 3, 0, 1, 1)
        self.label_15 = QtGui.QLabel(self.tab_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_3.addWidget(self.label_15, 3, 1, 1, 1)
        self.pyarchinit_progressBar_db = QtGui.QProgressBar(self.tab_2)
        self.pyarchinit_progressBar_db.setProperty(_fromUtf8("value"), 1)
        self.pyarchinit_progressBar_db.setAlignment(QtCore.Qt.AlignCenter)
        self.pyarchinit_progressBar_db.setOrientation(QtCore.Qt.Horizontal)
        self.pyarchinit_progressBar_db.setInvertedAppearance(False)
        self.pyarchinit_progressBar_db.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.pyarchinit_progressBar_db.setObjectName(_fromUtf8("pyarchinit_progressBar_db"))
        self.gridLayout_3.addWidget(self.pyarchinit_progressBar_db, 4, 0, 1, 1)
        self.pushButton_crea_layer = QtGui.QPushButton(self.tab_2)
        self.pushButton_crea_layer.setEnabled(True)
        self.pushButton_crea_layer.setObjectName(_fromUtf8("pushButton_crea_layer"))
        self.gridLayout_3.addWidget(self.pushButton_crea_layer, 4, 2, 2, 1)
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 2)
        self.pyarchinit_progressBar_template = QtGui.QProgressBar(self.tab_2)
        self.pyarchinit_progressBar_template.setProperty(_fromUtf8("value"), 1)
        self.pyarchinit_progressBar_template.setAlignment(QtCore.Qt.AlignCenter)
        self.pyarchinit_progressBar_template.setOrientation(QtCore.Qt.Horizontal)
        self.pyarchinit_progressBar_template.setInvertedAppearance(False)
        self.pyarchinit_progressBar_template.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.pyarchinit_progressBar_template.setObjectName(_fromUtf8("pyarchinit_progressBar_template"))
        self.gridLayout_3.addWidget(self.pyarchinit_progressBar_template, 6, 0, 1, 1)
        self.label_14 = QtGui.QLabel(self.tab_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_3.addWidget(self.label_14, 6, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 7, 0, 1, 2)
        self.pushButton_crea_layer_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_crea_layer_2.setEnabled(True)
        self.pushButton_crea_layer_2.setObjectName(_fromUtf8("pushButton_crea_layer_2"))
        self.gridLayout_3.addWidget(self.pushButton_crea_layer_2, 7, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 259, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 8, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_6.addWidget(self.label_11, 0, 1, 1, 1)
        self.pushButton_exp_directories = QtGui.QPushButton(self.tab_3)
        self.pushButton_exp_directories.setObjectName(_fromUtf8("pushButton_exp_directories"))
        self.gridLayout_6.addWidget(self.pushButton_exp_directories, 2, 1, 1, 1)
        self.line = QtGui.QFrame(self.tab_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_6.addWidget(self.line, 3, 1, 1, 5)
        self.comboBox_server_read = QtGui.QComboBox(self.tab_3)
        self.comboBox_server_read.setObjectName(_fromUtf8("comboBox_server_read"))
        self.comboBox_server_read.addItem(_fromUtf8(""))
        self.comboBox_server_read.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.comboBox_server_read, 7, 1, 1, 1)
        self.lineEdit_username_read = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_username_read.setObjectName(_fromUtf8("lineEdit_username_read"))
        self.gridLayout_6.addWidget(self.lineEdit_username_read, 8, 3, 1, 2)
        self.lineEdit_pass_read = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_pass_read.setObjectName(_fromUtf8("lineEdit_pass_read"))
        self.gridLayout_6.addWidget(self.lineEdit_pass_read, 8, 5, 1, 1)
        self.label_17 = QtGui.QLabel(self.tab_3)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_6.addWidget(self.label_17, 10, 1, 1, 1)
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_6.addWidget(self.label_18, 10, 3, 1, 1)
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_6.addWidget(self.label_19, 10, 5, 1, 1)
        self.label_22 = QtGui.QLabel(self.tab_3)
        self.label_22.setText(_fromUtf8(""))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.gridLayout_6.addWidget(self.label_22, 22, 5, 1, 1)
        self.comboBox_server_write = QtGui.QComboBox(self.tab_3)
        self.comboBox_server_write.setObjectName(_fromUtf8("comboBox_server_write"))
        self.comboBox_server_write.addItem(_fromUtf8(""))
        self.comboBox_server_write.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.comboBox_server_write, 28, 1, 1, 1)
        self.lineEdit_host_write = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_host_write.setObjectName(_fromUtf8("lineEdit_host_write"))
        self.gridLayout_6.addWidget(self.lineEdit_host_write, 29, 1, 1, 1)
        self.lineEdit_username_write = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_username_write.setObjectName(_fromUtf8("lineEdit_username_write"))
        self.gridLayout_6.addWidget(self.lineEdit_username_write, 29, 3, 1, 2)
        self.lineEdit_pass_write = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_pass_write.setObjectName(_fromUtf8("lineEdit_pass_write"))
        self.gridLayout_6.addWidget(self.lineEdit_pass_write, 29, 5, 1, 1)
        self.label_27 = QtGui.QLabel(self.tab_3)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_6.addWidget(self.label_27, 30, 1, 1, 1)
        self.label_28 = QtGui.QLabel(self.tab_3)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_6.addWidget(self.label_28, 30, 3, 1, 1)
        self.label_29 = QtGui.QLabel(self.tab_3)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_6.addWidget(self.label_29, 30, 5, 1, 1)
        self.lineEdit_database_write = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_database_write.setObjectName(_fromUtf8("lineEdit_database_write"))
        self.gridLayout_6.addWidget(self.lineEdit_database_write, 31, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.tab_3)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.gridLayout_6.addWidget(self.label_24, 32, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 68, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 34, 1, 1, 1)
        self.lineEdit_host_read = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_host_read.setObjectName(_fromUtf8("lineEdit_host_read"))
        self.gridLayout_6.addWidget(self.lineEdit_host_read, 8, 1, 1, 1)
        self.lineEdit_database_read = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_database_read.setObjectName(_fromUtf8("lineEdit_database_read"))
        self.gridLayout_6.addWidget(self.lineEdit_database_read, 12, 1, 1, 1)
        self.label_59 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_59.setFont(font)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.gridLayout_6.addWidget(self.label_59, 5, 1, 1, 1)
        self.label_60 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_60.setFont(font)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.gridLayout_6.addWidget(self.label_60, 6, 1, 1, 1)
        self.label_61 = QtGui.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_61.setFont(font)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.gridLayout_6.addWidget(self.label_61, 27, 1, 1, 1)
        self.pushButton_import = QtGui.QPushButton(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.pushButton_import.setFont(font)
        self.pushButton_import.setObjectName(_fromUtf8("pushButton_import"))
        self.gridLayout_6.addWidget(self.pushButton_import, 33, 5, 1, 1)
        self.label_20 = QtGui.QLabel(self.tab_3)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_6.addWidget(self.label_20, 13, 1, 1, 1)
        self.label_62 = QtGui.QLabel(self.tab_3)
        self.label_62.setObjectName(_fromUtf8("label_62"))
        self.gridLayout_6.addWidget(self.label_62, 18, 1, 1, 1)
        self.lineEdit_port_read = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_port_read.setObjectName(_fromUtf8("lineEdit_port_read"))
        self.gridLayout_6.addWidget(self.lineEdit_port_read, 12, 2, 1, 1)
        self.lineEdit_value_read = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_value_read.setObjectName(_fromUtf8("lineEdit_value_read"))
        self.gridLayout_6.addWidget(self.lineEdit_value_read, 15, 2, 1, 2)
        self.lineEdit_field_read = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_field_read.setObjectName(_fromUtf8("lineEdit_field_read"))
        self.gridLayout_6.addWidget(self.lineEdit_field_read, 15, 1, 1, 1)
        self.label_23 = QtGui.QLabel(self.tab_3)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.gridLayout_6.addWidget(self.label_23, 18, 2, 1, 1)
        self.label_25 = QtGui.QLabel(self.tab_3)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.gridLayout_6.addWidget(self.label_25, 13, 2, 1, 1)
        self.lineEdit_port_write = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_port_write.setObjectName(_fromUtf8("lineEdit_port_write"))
        self.gridLayout_6.addWidget(self.lineEdit_port_write, 31, 2, 1, 1)
        self.label_57 = QtGui.QLabel(self.tab_3)
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.gridLayout_6.addWidget(self.label_57, 32, 2, 1, 1)
        self.label_21 = QtGui.QLabel(self.tab_3)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.gridLayout_6.addWidget(self.label_21, 6, 3, 1, 1)
        self.comboBox_mapper_read = QtGui.QComboBox(self.tab_3)
        self.comboBox_mapper_read.setObjectName(_fromUtf8("comboBox_mapper_read"))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.comboBox_mapper_read.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.comboBox_mapper_read, 5, 3, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Dialog_Config)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Config)
        Dialog_Config.setTabOrder(self.comboBox_Database, self.lineEdit_Host)
        Dialog_Config.setTabOrder(self.lineEdit_Host, self.lineEdit_Port)
        Dialog_Config.setTabOrder(self.lineEdit_Port, self.lineEdit_DBname)
        Dialog_Config.setTabOrder(self.lineEdit_DBname, self.lineEdit_User)
        Dialog_Config.setTabOrder(self.lineEdit_User, self.lineEdit_Password)

    def retranslateUi(self, Dialog_Config):
        Dialog_Config.setWindowTitle(QtGui.QApplication.translate("Dialog_Config", "Impostazioni del sistema", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_Config", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_Database.setItemText(0, QtGui.QApplication.translate("Dialog_Config", "postgres", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_Database.setItemText(1, QtGui.QApplication.translate("Dialog_Config", "sqlite", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_Config", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_Host.setText(QtGui.QApplication.translate("Dialog_Config", "\'\'", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog_Config", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_Port.setText(QtGui.QApplication.translate("Dialog_Config", "\'\'", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_Config", "DBname", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_DBname.setText(QtGui.QApplication.translate("Dialog_Config", "\'\'", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog_Config", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_User.setText(QtGui.QApplication.translate("Dialog_Config", "\'\'", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog_Config", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setText(QtGui.QApplication.translate("Dialog_Config", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_Logo_path.setText(QtGui.QApplication.translate("Dialog_Config", "\'\'", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("Dialog_Config", "Logo path", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_Thumb_path.setText(QtGui.QApplication.translate("Dialog_Config", "\'\'", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog_Config", "Thumbnail path", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_experimental.setItemText(0, QtGui.QApplication.translate("Dialog_Config", "Si", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_experimental.setItemText(1, QtGui.QApplication.translate("Dialog_Config", "No", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("Dialog_Config", "Experimental", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog_Config", "Parametri di connessione", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog_Config", "Installa il database", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_dbname.setText(QtGui.QApplication.translate("Dialog_Config", "pyarchinit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setToolTip(QtGui.QApplication.translate("Dialog_Config", "<html><head/><body><p><span style=\" font-size:10pt;\">Puoi inserire un nome differente da quello presente</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog_Config", "inserisci nome db", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_crea_database.setText(QtGui.QApplication.translate("Dialog_Config", "Installa", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_template_postgis.setText(QtGui.QApplication.translate("Dialog_Config", "template_postgis_20", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setToolTip(QtGui.QApplication.translate("Dialog_Config", "<html><head/><body><p>qui devi inserire il nome del template che vuoi usare. Ricorda di usare il template specifico a seconda di quale postgis usi</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Dialog_Config", "inserisci nome template", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_port_db.setText(QtGui.QApplication.translate("Dialog_Config", "5432", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setToolTip(QtGui.QApplication.translate("Dialog_Config", "<html><head/><body><p><span style=\" font-size:10pt;\">puoi inserire il numero di porta differente</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("Dialog_Config", "inserisci numero porta", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_crea_layer.setText(QtGui.QApplication.translate("Dialog_Config", "Installa", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog_Config", "Installa il db geografico su Postgres per postgis 1.5", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("Dialog_Config", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">OPPURE</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog_Config", "Installa il db geografico su Postgres per postgis 2.x", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_crea_layer_2.setText(QtGui.QApplication.translate("Dialog_Config", "Installa", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog_Config", "Installazione layers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Dialog_Config", "Esportazione directories", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_exp_directories.setText(QtGui.QApplication.translate("Dialog_Config", "Esportazione experimental", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_server_read.setItemText(0, QtGui.QApplication.translate("Dialog_Config", "sqlite", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_server_read.setItemText(1, QtGui.QApplication.translate("Dialog_Config", "postgres", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("Dialog_Config", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("Dialog_Config", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("Dialog_Config", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_server_write.setItemText(0, QtGui.QApplication.translate("Dialog_Config", "postgres", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_server_write.setItemText(1, QtGui.QApplication.translate("Dialog_Config", "sqlite", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("Dialog_Config", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("Dialog_Config", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("Dialog_Config", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("Dialog_Config", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label_59.setText(QtGui.QApplication.translate("Dialog_Config", "Importazione dati", None, QtGui.QApplication.UnicodeUTF8))
        self.label_60.setText(QtGui.QApplication.translate("Dialog_Config", "FROM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_61.setText(QtGui.QApplication.translate("Dialog_Config", "TO", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_import.setText(QtGui.QApplication.translate("Dialog_Config", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("Dialog_Config", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label_62.setText(QtGui.QApplication.translate("Dialog_Config", "Nome campo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("Dialog_Config", "Valore", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("Dialog_Config", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_57.setText(QtGui.QApplication.translate("Dialog_Config", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("Dialog_Config", "Mappatura pyArchInit", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(0, QtGui.QApplication.translate("Dialog_Config", "US", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(1, QtGui.QApplication.translate("Dialog_Config", "UT", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(2, QtGui.QApplication.translate("Dialog_Config", "SITE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(3, QtGui.QApplication.translate("Dialog_Config", "PERIODIZZAZIONE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(4, QtGui.QApplication.translate("Dialog_Config", "INVENTARIO_MATERIALI", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(5, QtGui.QApplication.translate("Dialog_Config", "STRUTTURA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(6, QtGui.QApplication.translate("Dialog_Config", "TAFONOMIA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(7, QtGui.QApplication.translate("Dialog_Config", "PYARCHINIT_THESAURUS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(8, QtGui.QApplication.translate("Dialog_Config", "SCHEDAIND", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(9, QtGui.QApplication.translate("Dialog_Config", "DETSESSO", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(10, QtGui.QApplication.translate("Dialog_Config", "DETETA", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(11, QtGui.QApplication.translate("Dialog_Config", "ARCHEOZOOLOGY", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(12, QtGui.QApplication.translate("Dialog_Config", "CAMPIONI", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mapper_read.setItemText(13, QtGui.QApplication.translate("Dialog_Config", "DOCUMENTAZIONE", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Dialog_Config", "Tool di amministrazione", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc