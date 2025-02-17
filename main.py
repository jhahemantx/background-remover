import cv2
import os
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# imgBackground = cv2.imread("Images/2.jpg")

listImg = os.listdir("Images")
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'Images/{imgPath}')
    imgList.append(img)
index, n = 0, len(imgList)



segmentor = SelfiSegmentation(1) 


while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgList[index], ) 

    cv2.imshow("imgOut", imgOut)
    key = cv2.waitKey(1)
    

    if key == ord('a'):
        if index==0:
            index = n
        index -=1
    elif key == ord('d'):
        if index== n-1:
            index=-1
        index+=1
    elif key == ord('q'):
        break

