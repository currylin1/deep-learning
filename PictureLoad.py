import platform

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw,Image
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QPixmap


class PictureLoad(QThread):
    callback=Signal(object)

    def __init__(self,path_1,parent=None):
        super().__init__(parent)
        self.path_1=path_1
        self.runFlag = True


    def text(self, img, text, xy=(0, 0), color=(0, 0, 0), size=12):
        pil = Image.fromarray(img)
        s = platform.system()
        if s == "Linux":
            font = ImageFont.truetype(
                '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc',
                size)
        elif s == "Darwin":
            font = ImageFont.truetype('....', size)
        else:
            font = ImageFont.truetype('simsun.ttc', size)
        ImageDraw.Draw(pil).text(xy, text, font=font, fill=color)
        return np.array(pil)



    def run(self): #新執行續要做的工作

        if self.runFlag:
            img = cv2.imdecode(
                np.fromfile(self.path_1, dtype=np.uint8),
                cv2.IMREAD_COLOR
            )[:, :, ::-1].copy()
            self.callback.emit(img)
        else:
            pass



        index=0




