# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/draw.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1087, 814)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1071, 771))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.layoutWidget = QtWidgets.QWidget(self.tab_1)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1051, 724))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.line_3 = QtWidgets.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 6, 1, 1, 2)
        self.button_draw = QtWidgets.QPushButton(self.layoutWidget)
        self.button_draw.setMinimumSize(QtCore.QSize(100, 30))
        self.button_draw.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.button_draw.setFont(font)
        self.button_draw.setObjectName("button_draw")
        self.gridLayout.addWidget(self.button_draw, 5, 2, 1, 1)
        self.textEdit_y1 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_y1.setMinimumSize(QtCore.QSize(100, 30))
        self.textEdit_y1.setMaximumSize(QtCore.QSize(200, 30))
        self.textEdit_y1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_y1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textEdit_y1.setTabChangesFocus(True)
        self.textEdit_y1.setObjectName("textEdit_y1")
        self.gridLayout.addWidget(self.textEdit_y1, 2, 2, 1, 1)
        self.label_image = QtWidgets.QLabel(self.layoutWidget)
        self.label_image.setMinimumSize(QtCore.QSize(600, 600))
        self.label_image.setMaximumSize(QtCore.QSize(600, 600))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_image.setFont(font)
        self.label_image.setAcceptDrops(True)
        self.label_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_image.setLineWidth(2)
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.gridLayout.addWidget(self.label_image, 0, 0, 14, 1)
        self.textEdit_in_file = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_in_file.setMinimumSize(QtCore.QSize(100, 30))
        self.textEdit_in_file.setMaximumSize(QtCore.QSize(200, 30))
        self.textEdit_in_file.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_in_file.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textEdit_in_file.setWhatsThis("")
        self.textEdit_in_file.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit_in_file.setTabChangesFocus(False)
        self.textEdit_in_file.setReadOnly(False)
        self.textEdit_in_file.setObjectName("textEdit_in_file")
        self.gridLayout.addWidget(self.textEdit_in_file, 11, 1, 1, 1)
        self.textEdit_x2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_x2.setMinimumSize(QtCore.QSize(100, 30))
        self.textEdit_x2.setMaximumSize(QtCore.QSize(200, 30))
        self.textEdit_x2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_x2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textEdit_x2.setTabChangesFocus(True)
        self.textEdit_x2.setObjectName("textEdit_x2")
        self.gridLayout.addWidget(self.textEdit_x2, 3, 2, 1, 1)
        self.label_input = QtWidgets.QLabel(self.layoutWidget)
        self.label_input.setMinimumSize(QtCore.QSize(200, 50))
        self.label_input.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_input.setFont(font)
        self.label_input.setObjectName("label_input")
        self.gridLayout.addWidget(self.label_input, 0, 1, 1, 2)
        self.label_y2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_y2.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.label_y2.setFont(font)
        self.label_y2.setTextFormat(QtCore.Qt.AutoText)
        self.label_y2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_y2.setObjectName("label_y2")
        self.gridLayout.addWidget(self.label_y2, 4, 1, 1, 1)
        self.textEdit_y2 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_y2.setMinimumSize(QtCore.QSize(100, 30))
        self.textEdit_y2.setMaximumSize(QtCore.QSize(200, 30))
        self.textEdit_y2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_y2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textEdit_y2.setTabChangesFocus(True)
        self.textEdit_y2.setObjectName("textEdit_y2")
        self.gridLayout.addWidget(self.textEdit_y2, 4, 2, 1, 1)
        self.label_x1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_x1.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.label_x1.setFont(font)
        self.label_x1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x1.setObjectName("label_x1")
        self.gridLayout.addWidget(self.label_x1, 1, 1, 1, 1)
        self.label_x2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_x2.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.label_x2.setFont(font)
        self.label_x2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x2.setObjectName("label_x2")
        self.gridLayout.addWidget(self.label_x2, 3, 1, 1, 1)
        self.label_boxes = QtWidgets.QLabel(self.layoutWidget)
        self.label_boxes.setMinimumSize(QtCore.QSize(200, 50))
        self.label_boxes.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_boxes.setFont(font)
        self.label_boxes.setObjectName("label_boxes")
        self.gridLayout.addWidget(self.label_boxes, 7, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 9, 1, 1, 2)
        self.textEdit_out_file = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_out_file.setMinimumSize(QtCore.QSize(100, 30))
        self.textEdit_out_file.setMaximumSize(QtCore.QSize(200, 30))
        self.textEdit_out_file.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_out_file.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textEdit_out_file.setWhatsThis("")
        self.textEdit_out_file.setInputMethodHints(QtCore.Qt.ImhNone)
        self.textEdit_out_file.setTabChangesFocus(False)
        self.textEdit_out_file.setReadOnly(False)
        self.textEdit_out_file.setPlaceholderText("")
        self.textEdit_out_file.setObjectName("textEdit_out_file")
        self.gridLayout.addWidget(self.textEdit_out_file, 12, 1, 1, 1)
        self.button_save = QtWidgets.QPushButton(self.layoutWidget)
        self.button_save.setMinimumSize(QtCore.QSize(100, 30))
        self.button_save.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.button_save.setFont(font)
        self.button_save.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_save.setObjectName("button_save")
        self.gridLayout.addWidget(self.button_save, 12, 2, 1, 1)
        self.button_load = QtWidgets.QPushButton(self.layoutWidget)
        self.button_load.setMinimumSize(QtCore.QSize(100, 30))
        self.button_load.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.button_load.setFont(font)
        self.button_load.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_load.setObjectName("button_load")
        self.gridLayout.addWidget(self.button_load, 11, 2, 1, 1)
        self.label_image_name = QtWidgets.QLabel(self.layoutWidget)
        self.label_image_name.setMinimumSize(QtCore.QSize(300, 50))
        self.label_image_name.setMaximumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_image_name.setFont(font)
        self.label_image_name.setObjectName("label_image_name")
        self.gridLayout.addWidget(self.label_image_name, 10, 1, 1, 2)
        self.listWidget_box = QtWidgets.QListWidget(self.layoutWidget)
        self.listWidget_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget_box.setObjectName("listWidget_box")
        self.gridLayout.addWidget(self.listWidget_box, 8, 1, 1, 2)
        self.button_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.button_clear.setMinimumSize(QtCore.QSize(100, 30))
        self.button_clear.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.button_clear.setFont(font)
        self.button_clear.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_clear.setObjectName("button_clear")
        self.gridLayout.addWidget(self.button_clear, 7, 2, 1, 1)
        self.label_y1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_y1.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.label_y1.setFont(font)
        self.label_y1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_y1.setObjectName("label_y1")
        self.gridLayout.addWidget(self.label_y1, 2, 1, 1, 1)
        self.button_draw_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.button_draw_2.setMinimumSize(QtCore.QSize(100, 30))
        self.button_draw_2.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        font.setPointSize(10)
        self.button_draw_2.setFont(font)
        self.button_draw_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button_draw_2.setObjectName("button_draw_2")
        self.gridLayout.addWidget(self.button_draw_2, 5, 1, 1, 1)
        self.textEdit_x1 = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_x1.setMinimumSize(QtCore.QSize(100, 30))
        self.textEdit_x1.setMaximumSize(QtCore.QSize(200, 30))
        self.textEdit_x1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textEdit_x1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.textEdit_x1.setTabChangesFocus(True)
        self.textEdit_x1.setObjectName("textEdit_x1")
        self.gridLayout.addWidget(self.textEdit_x1, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1051, 731))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_save = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout_2.addWidget(self.pushButton_save, 1, 10, 1, 1)
        self.pushButton_load = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_load.setObjectName("pushButton_load")
        self.gridLayout_2.addWidget(self.pushButton_load, 1, 4, 1, 1)
        self.textEdit_in_h = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_in_h.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_in_h.setObjectName("textEdit_in_h")
        self.gridLayout_2.addWidget(self.textEdit_in_h, 2, 4, 1, 1)
        self.textEdit_out_w = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_out_w.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_out_w.setObjectName("textEdit_out_w")
        self.gridLayout_2.addWidget(self.textEdit_out_w, 2, 8, 1, 1)
        self.label_h = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_h.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_h.setFont(font)
        self.label_h.setAlignment(QtCore.Qt.AlignCenter)
        self.label_h.setObjectName("label_h")
        self.gridLayout_2.addWidget(self.label_h, 2, 3, 1, 1)
        self.label_w_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_w_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_w_2.setFont(font)
        self.label_w_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_w_2.setObjectName("label_w_2")
        self.gridLayout_2.addWidget(self.label_w_2, 2, 7, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 0, 6, 5, 1)
        self.label_w_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_w_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_w_3.setFont(font)
        self.label_w_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_w_3.setObjectName("label_w_3")
        self.gridLayout_2.addWidget(self.label_w_3, 2, 9, 1, 1)
        self.label_w = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_w.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_w.setFont(font)
        self.label_w.setAlignment(QtCore.Qt.AlignCenter)
        self.label_w.setObjectName("label_w")
        self.gridLayout_2.addWidget(self.label_w, 2, 1, 1, 1)
        self.pushButton_resize = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_resize.setObjectName("pushButton_resize")
        self.gridLayout_2.addWidget(self.pushButton_resize, 3, 10, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 4)
        self.textEdit_out_h = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_out_h.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_out_h.setObjectName("textEdit_out_h")
        self.gridLayout_2.addWidget(self.textEdit_out_h, 2, 10, 1, 1)
        self.textEdit_in_w = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_in_w.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_in_w.setObjectName("textEdit_in_w")
        self.gridLayout_2.addWidget(self.textEdit_in_w, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 7, 1, 4)
        self.textEdit_in_image = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_in_image.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_in_image.setObjectName("textEdit_in_image")
        self.gridLayout_2.addWidget(self.textEdit_in_image, 1, 2, 1, 2)
        self.label_w_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_w_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_w_4.setFont(font)
        self.label_w_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_w_4.setObjectName("label_w_4")
        self.gridLayout_2.addWidget(self.label_w_4, 1, 1, 1, 1)
        self.textEdit_out_image = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_out_image.setMaximumSize(QtCore.QSize(16777215, 30))
        self.textEdit_out_image.setObjectName("textEdit_out_image")
        self.gridLayout_2.addWidget(self.textEdit_out_image, 1, 8, 1, 2)
        self.label_w_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_w_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_w_5.setFont(font)
        self.label_w_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_w_5.setObjectName("label_w_5")
        self.gridLayout_2.addWidget(self.label_w_5, 1, 7, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(516, 516))
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 1, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(516, 516))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 7, 1, 4)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1087, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.textEdit_x1, self.textEdit_y1)
        MainWindow.setTabOrder(self.textEdit_y1, self.textEdit_x2)
        MainWindow.setTabOrder(self.textEdit_x2, self.textEdit_y2)
        MainWindow.setTabOrder(self.textEdit_y2, self.button_draw)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Draw Prediction Box"))
        self.button_draw.setText(_translate("MainWindow", "Draw"))
        self.textEdit_y1.setPlaceholderText(_translate("MainWindow", "Top"))
        self.label_image.setText(_translate("MainWindow", "<html><head/><body><p>Drag and drop jpg file to right down textbox</p><p>&amp; Press &quot;Load&quot; !!</p></body></html>"))
        self.textEdit_in_file.setPlaceholderText(_translate("MainWindow", "Drop jpg image here"))
        self.textEdit_x2.setPlaceholderText(_translate("MainWindow", "Right"))
        self.label_input.setText(_translate("MainWindow", "Input box coordinate"))
        self.label_y2.setText(_translate("MainWindow", "y2"))
        self.textEdit_y2.setPlaceholderText(_translate("MainWindow", "Bottom"))
        self.label_x1.setText(_translate("MainWindow", "x1"))
        self.label_x2.setText(_translate("MainWindow", "x2"))
        self.label_boxes.setText(_translate("MainWindow", "Drawn Detection Boxes"))
        self.button_save.setText(_translate("MainWindow", "Save"))
        self.button_load.setText(_translate("MainWindow", "Load"))
        self.label_image_name.setText(_translate("MainWindow", "Load & Save Image"))
        self.button_clear.setText(_translate("MainWindow", "Clear"))
        self.label_y1.setText(_translate("MainWindow", "y1"))
        self.button_draw_2.setText(_translate("MainWindow", "Color"))
        self.textEdit_x1.setPlaceholderText(_translate("MainWindow", "Left"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Draw bb box"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "<html><head/><body><p>Enter the bounding box</p><p>It will be drawn on the image</p></body></html>"))
        self.pushButton_save.setText(_translate("MainWindow", "Save"))
        self.pushButton_load.setText(_translate("MainWindow", "Load"))
        self.textEdit_out_w.setPlaceholderText(_translate("MainWindow", "Resized width"))
        self.label_h.setText(_translate("MainWindow", "Height"))
        self.label_w_2.setText(_translate("MainWindow", "Width"))
        self.label_w_3.setText(_translate("MainWindow", "Height"))
        self.label_w.setText(_translate("MainWindow", "Width"))
        self.pushButton_resize.setText(_translate("MainWindow", "Resize"))
        self.label.setText(_translate("MainWindow", "Original Image"))
        self.textEdit_out_h.setPlaceholderText(_translate("MainWindow", "Resized height"))
        self.label_2.setText(_translate("MainWindow", "Resized Image"))
        self.textEdit_in_image.setPlaceholderText(_translate("MainWindow", "Drop jpg file in here"))
        self.label_w_4.setText(_translate("MainWindow", "File"))
        self.label_w_5.setText(_translate("MainWindow", "File"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Resize"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "<html><head/><body><p>Resize the input image</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
