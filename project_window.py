import sys
import time

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap, QImage
from PySide6.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QPushButton, QFileDialog

from Mixpicture import Mixpicture
from PictureLoad import PictureLoad
from PictureLoad_2 import PictureLoad_2
from ui.untitled import Ui_MainWindow


class project(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.path_1="C:/python_ai/project_work/starry_night.jpg"
        self.path_2 = "C:/python_ai/project_work/645017.jpg"
        #預設圖片
        self.pictureload = PictureLoad(self.path_1)
        self.pictureload.callback.connect(self.pictureloadCallback)
        self.pictureload.start()

        self.pictureload_2 = PictureLoad_2(self.path_2)
        self.pictureload_2.callback.connect(self.pictureloadCallback_2)
        self.pictureload_2.start()


        self.btnPicture_1.clicked.connect(self.btnPicture_1Click)
        self.btnPicture_2.clicked.connect(self.btnPicture_2Click)
        self.btnStart.clicked.connect(self.btnStartClick)

        self.mixpicture = None


    def btnPicture_2Click(self):
        path_2, _ = QFileDialog.getOpenFileName(None, "Select Image File", "")

        if path_2 !="":
            self.path_2=path_2.replace("\\","/")
            self.pictureload.runFlag=False


            time.sleep(0.01)
            self.pictureload_2=PictureLoad(self.path_2)
            self.pictureload_2.callback.connect(self.pictureloadCallback_2)
            self.pictureload_2.start()
            print(self.path_2)



    def btnPicture_1Click(self):
        path_1, _ = QFileDialog.getOpenFileName(None, "Select Image File", "")
        if path_1 !="":
            self.path_1=path_1.replace("\\","/")
            self.pictureload.runFlag=False


            time.sleep(0.01)
            self.pictureload=PictureLoad(self.path_1)
            self.pictureload.callback.connect(self.pictureloadCallback)
            self.pictureload.start()
            print(self.path_1)




    def btnStartClick(self):

        if self.mixpicture is not None:
            self.mixpicture.runFlag=False
            time.sleep(1)




        self.lblStatus.setText("融合準備中")
        self.mixpicture = Mixpicture(self.path_1,self.path_2)
        self.mixpicture.start()


        self.mixpicture.callback.connect(self.mixpicturecallback)


    def pictureloadCallback(self, img):

        image = img[:,:, ::-1].copy()  # Assuming img is a NumPy array in BGR format
        pix = QPixmap(
            QImage(
                image,
                img.shape[1],
                img.shape[0],
                img.shape[1] * 3,
                QImage.Format_BGR888
            )
        )
        pr = pix.width() / pix.height()
        lr = self.lblPicture_1.width() / self.lblPicture_1.height()
        if pr > lr:
            pix = pix.scaled(self.lblPicture_1.width(), int(self.lblPicture_1.width() / pr))
        else:
            pix = pix.scaled(int(self.lblPicture_1.height() * lr), self.lblPicture_1.height())
        self.lblPicture_1.setPixmap(pix)


    def pictureloadCallback_2(self, img):

        image = img[:,:, ::-1].copy()  # Assuming img is a NumPy array in BGR format
        pix = QPixmap(
            QImage(
                image,
                img.shape[1],
                img.shape[0],
                img.shape[1] * 3,
                QImage.Format_BGR888
            )
        )
        pr = pix.width() / pix.height()
        lr = self.lblPicture_2.width() / self.lblPicture_2.height()
        if pr > lr:
            pix = pix.scaled(self.lblPicture_2.width(), int(self.lblPicture_2.width() / pr))
        else:
            pix = pix.scaled(int(self.lblPicture_2.height() * lr), self.lblPicture_2.height())
        self.lblPicture_2.setPixmap(pix)

    def mixpicturecallback(self,img,s):




        image = img[:, :, ::-1].copy()
        pix = QPixmap(
            QImage(
                image,
                img.shape[1],
                img.shape[0],
                img.shape[1] * 3,
                QImage.Format_BGR888
            )
        )
        pr = pix.width() / pix.height()
        lr = self.lblPicture_3.width() / self.lblPicture_3.height()
        if pr > lr:
            pix = pix.scaled(self.lblPicture_3.width(), int(self.lblPicture_3.width() / pr))
        else:
            pix = pix.scaled(int(self.lblPicture_3.height() * lr), self.lblPicture_3.height())
        self.lblPicture_3.setPixmap(pix)

        self.lblStatus.setText(f"融合完成度：{s}%")

    def closeEvent(self, event):
        if self.mixpicture is not None:
            self.mixpicture.runFlag=False
            time.sleep(0.01)

            print("已關閉")




app=QApplication(sys.argv)
w=project()
w.show()
app.exec()