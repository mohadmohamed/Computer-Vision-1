# import cv2 : image shaping
# #chapter 3
# #Resizing image and get size of image
# img = cv2.imread("Resources/Images/white Ferrari in space.jpeg")


# imgresized = cv2.resize(img,(240,426)) #width then height
# print(img.shape) #height width BGR 
# print(imgresized.shape) #height width BGR 

# #crop image
# croppedimg = img[200:1000, 200: 700]  #height then width

# cv2.imshow("image", img) 
# cv2.imshow("resized image", imgresized) 
# cv2.imshow("cropped img",croppedimg)
# cv2.waitKey(0)

#chapter 4 : shapes and txt
# import cv2
# import numpy as np
# #0:black 1:white

#create black img
# img = np.zeros((512,512,3), np.uint8) 
# # print(img)
# # img[:] = 255,0,0

# cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
# cv2.rectangle(img,(0,0), (250,350),(255, 0, 0), cv2.FILLED)
# cv2.circle(img, (250,250), 30 ,(255, 0, 255), cv2.FILLED)
# cv2.putText(img,"THIS IS A TEXT ON IMG", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1,(255, 255, 255) )

# cv2.imshow("img",img)
# cv2.waitKey(0)

#Chapter 5 : Warp Prespective

import cv2 as c
import numpy as np

img = c.imread("Resources/Images/image.png")

#corner points
width, height = 250,350
pts1 = np.float32([[77,147],[193,128],[105,324],[238,296]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = c.getPerspectiveTransform(pts1, pts2)

imgout = c.warpPerspective(img , matrix, (width,height))

c.imshow("out",imgout)
c.imshow("img",img)

c.waitKey(0)