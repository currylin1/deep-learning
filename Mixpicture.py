
import os
import shutil
import pylab as plt
from PySide6.QtCore import QThread, Signal

from keras.optimizers import SGD
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import keras
from keras.applications import VGG19
import cv2
import numpy as np
from keras.applications.vgg19 import preprocess_input
import tensorflow as tf

class Mixpicture(QThread):
    callback=Signal(object,int)

    def __init__(self,path_1,path_2,parent=None,):
        super().__init__(parent)
        self.path_1=path_1
        self.path_2=path_2
        self.model = VGG19(weights='imagenet', include_top=False)
        self.outputs = dict([layer.name, layer.output] for layer in self.model.layers)
        self.model = keras.Model(inputs=self.model.inputs, outputs=self.outputs)
        self.content_layer_name = 'block5_conv2'
        self.style_layer_names = [
            'block1_conv1',
            'block2_conv1',
            'block3_conv1',
            'block4_conv1',
            'block5_conv1',
        ]
        self.total_variation_weight = 1e-6
        self.style_weight = 1e-6 / len(self.style_layer_names)
        self.content_weight = 2.5e-8
        self.epochs = 100

        self.runFlag = True




    def deprocess_image(self,img):
        img=img.reshape((self.height, self.width, 3))[:,:,::-1].copy()
        img[:, :, 0] += 123.68
        img[:, :, 1] += 116.779
        img[:, :, 2] += 109.939
        img = np.clip(img, 0,255).astype(np.uint8)
        return img

    def total_variation_loss(self,x):
        a = tf.square(
            x[:, : height - 1, : width - 1, :] - x[:, 1:, : width - 1, :]
        )
        b = tf.square(
            x[:, : height - 1, : width - 1, :] - x[:, : height - 1, 1:, :]
        )
        return tf.reduce_sum(tf.pow(a + b, 1.25))
    def gram_matrix(self,x):
        self.x=tf.reshape(x, (x.shape[1], x.shape[2], x.shape[3]))#四維轉三維
        self.x=tf.transpose(self.x, (2,0,1))#Channel, width, height
        self.features=tf.reshape(self.x, (tf.shape(self.x)[0], -1))
        self.gram=tf.matmul(self.features, tf.transpose(self.features))
        return self.gram
    def style_loss(self,style_feature, combination_feature):
        # s=style_feature
        # c=combination_feature
        self.s=self.gram_matrix(style_feature)
        self.c=self.gram_matrix(combination_feature)
        self.size=self.width*self.height
        self.channels=3

        return tf.reduce_sum(tf.square(self.s-self.c))/(4*(self.channels**2)*(self.size**2))
    def compute_loss_and_grads(self,combination_image, base_image, style_image):
        with tf.GradientTape() as tape:

            self.base_features=self.model(base_image)
            self.base_feature=self.base_features[self.content_layer_name]
            self.loss=tf.zeros(shape=())
            self.combination_features=self.model(combination_image)
            self.combination_feature=self.combination_features[self.content_layer_name]

            self.loss= self.loss+self.content_weight * tf.reduce_sum(
                tf.square(self.base_feature-self.combination_feature)
            )
            self.style_features=self.model(style_image)
            for layer in self.style_layer_names:
                self.combination_feature=self.combination_features[layer]
                self.style_feature=self.style_features[layer]

                self.style_loss_value= self.style_loss(self.style_feature, self.combination_feature)
                self.loss += self.style_loss_value * self.style_weight
        self.grads=tape.gradient(self.loss, self.combination_image)
        return self.loss, self.grads

    def run(self):

        self.base_image=cv2.imdecode(
            np.fromfile(self.path_2, dtype=np.uint8),
            cv2.IMREAD_COLOR
        )[:,:,::-1].copy()
        self.h, self.w, _ = self.base_image.shape
        self.height = 300#ram 不足 12G 的人，請改為 600 或更小
        self.width = round(self.w/self.h*self.height)
        self.base_image = cv2.resize(
            self.base_image,
            (self.width, self.height),
            interpolation=cv2.INTER_LINEAR
        )
        self.base_image=np.expand_dims(self.base_image, axis=0)
        self.base_image=preprocess_input(self.base_image)

        self.style_image=cv2.imdecode(
            np.fromfile(self.path_1, dtype=np.uint8),
            cv2.IMREAD_COLOR
        )[:,:,::-1].copy()
        self.style_image = cv2.resize(
            self.style_image,
            (self.width, self.height),
            interpolation=cv2.INTER_LINEAR
        )
        self.style_image=np.expand_dims(self.style_image, axis=0)
        self.style_image=preprocess_input(self.style_image)
        self.combination_image=tf.Variable(self.base_image)

        self.optimizer=SGD(
            tf.keras.optimizers.schedules.ExponentialDecay(
                initial_learning_rate=100.0,
                decay_steps=100,
                decay_rate=0.96
            )
        )
        self.output_path="./output"
        if os.path.exists(self.output_path):
            shutil.rmtree(self.output_path)
        os.mkdir(self.output_path)

        x=0

        while self.runFlag and x<=self.epochs:
            self.loss, self.grads=self.compute_loss_and_grads(self.combination_image, self.base_image, self.style_image)

            self.optimizer.apply_gradients([(self.grads, self.combination_image)])#更改合成照裏面的值
            print(f"epoch : {x}")
            img=self.deprocess_image((self.combination_image).numpy())#轉換成圖型



            #每 100 次儲存一次圖片
            if x == self.epochs:
                file=os.path.join(self.output_path, f'combination_epoch{x}.jpg')
                keras.utils.save_img(file, img)
            s=int((x/self.epochs)*100)

            self.callback.emit(img,s)
            x += 1






