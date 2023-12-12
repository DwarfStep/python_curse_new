import pandas as pd
from sklearn import svm
import cv2 as cv
from resize import resizing
import numpy as np

# 1 point


class Video_detect:

    def __init__(self, video_f, new_wigth=None, new_height=None):
        self.new_wigth = new_wigth
        self.new_height = new_height
        self.frame = None
        self.video_f = video_f


    def detect_and_display(self):
        face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

        frame_gray = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)

        faces = face_cascade.detectMultiScale(frame_gray)

        for (x, y, w, h) in faces:
            center = (x + w // 2, y + h // 2)
            self.frame = cv.ellipse(self.frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
            self.frame = resizing(self.frame, new_wigth= self.new_wigth, new_height=self.new_height)
            cv.imshow('Capture - Face detection', self.frame)



    def infernce(self):
        camera_device = self.video_f
        cap = cv.VideoCapture(camera_device)

        if not cap.isOpened():
            raise Exception('error open')
        return cap

    def show_v(self, cap):
        while True:
            read, self.frame = cap.read()
            if not read:
                raise Exception('error')
            self.detect_and_display()
            if cv.waitKey(10) == ord('q'):
                break


a = Video_detect('video_1.mp4', new_wigth=600)
cap = a.infernce()
a.show_v(cap)



# 2 point
digits = pd.read_csv('titanic.csv').to_numpy()
print(digits)
model = svm.SVC(gamma=1)
testt = digits[:, (0, 3, 6)]
for i in range(len(digits[:, (0, 3, 6)])):
    for j in range(3):
        testt[i][j] = float(testt[i][j])
X_train = testt
y_train = digits[:, -2]
print(X_train)
model.fit(X_train, y_train)
predicted = model.predict(X_train[:20])

Y_test = y_train[:20]
print('Предсказание Сети')
print(predicted)
print('\nПравильные ответы')
print(Y_test)