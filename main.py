from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from UI import draw_ui, save_ui
import cv2
import time

class Main(QMainWindow, draw_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_draw.clicked.connect(self.draw_box)
        self.button_load.clicked.connect(self.load_image)
        self.button_clear.clicked.connect(self.clear)
        self.button_save.clicked.connect(self.save_image)
        self.file_path = ""
        self.file_name = ""
        self.box_count = 0
        self.img = None
            
    def load_image(self):
        ## get file name
        img_file = self.textEdit_in_file.toPlainText()
        img_file = img_file.split("///")[-1]
        file_path = "/".join(img_file.split("/")[:-1])+"/"
        file_name = img_file.split("/")[-1]
        
        self.ori_img = cv2.imread(img_file)
        if self.ori_img is not None:
            self.textEdit_in_file.setText(file_path + file_name)
            self.textEdit_out_file.setText(file_path + "predicted_" + file_name)
            self.label_image.setText("")
            self.img = self.ori_img.copy()
            self.show_image()
        else:
            self.label_image.setText("Load image faill !!")
        

    def show_image(self):
        ## resize, fit label size
        img_h, img_w, _ = self.img.shape  
        label_w = self.label_image.size().width()
        label_h = self.label_image.size().height()
        if img_w>img_h:
            ratio = label_w/img_w
        else:
            ratio = label_h/img_h
        resized_img = cv2.resize(self.img, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_AREA)

        ## show image with opencv
        # cv2.imshow('My Image', self.img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        ## to qt image
        bytesPerline = 3 * resized_img.shape[1]
        qImg = QImage(resized_img.data, resized_img.shape[1], resized_img.shape[0], bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.label_image.setPixmap(QPixmap.fromImage(qImg))

    def draw_box(self):          
        if self.img is not None:
            x1 = self.textEdit_x1.toPlainText()
            y1 = self.textEdit_y1.toPlainText()
            x2 = self.textEdit_x2.toPlainText()
            y2 = self.textEdit_y2.toPlainText()
            ## add box to list
            self.box_count += 1
            self.listWidget_box.addItem("Box "+str(self.box_count)+": ("+", ".join([x1,y1,x2,y2])+")")
            ## draw image
            self.label_image.setText("")
            cv2.rectangle(self.img, (int(x1),int(y1)), (int(x2),int(y2)), (0,0,255), 5)
            self.show_image()
        else:
            self.label_image.setText("Load image first!!")

    def clear(self):
        ## clear box list
        self.listWidget_box.clear()
        ## draw ori image
        self.img = self.ori_img.copy()
        self.show_image()

    def save_image(self):
        out_file = self.textEdit_out_file.toPlainText()
        cv2.imwrite(out_file, self.img)
        save_window.show()

class Dialog(QDialog, save_ui.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    save_window = Dialog()
    sys.exit(app.exec_())