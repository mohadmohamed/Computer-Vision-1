# import cv2
# import numpy as np
# print("package is imported")

# #CHAPTER 1
# #--------
# # read image
# # img = cv2.imread("Resources/Images/white Ferrari in space.jpeg")
# # cv2.imshow("output",img)
# # cv2.waitKey(0)

# # read video
# # vid = cv2.VideoCapture("Resources/Videos/SampleVideo_1280x720_1mb.mp4")
# # while True:
# #     bool, img = vid.read()
# #     cv2.imshow("Video", img)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break

# #read camera
# # cam = cv2.VideoCapture(0)
# # cam.set(3,640) #width
# # cam.set(4,480) #height
# # cam.set(10,1200) #brightness

# # while True:
# #     bool, img = cam.read()
# #     cv2.imshow("camera", img)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break

# #CHAPTER 2
# #---------

# #gray and blur image
# img = cv2.imread("Resources/Images/white Ferrari in space.jpeg")
# kernel = np.ones((5, 5), np.uint8) # 0 to 255

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
# imgBlur = cv2.GaussianBlur(imgGray, (11,11),0) #only odd numbers
# imgCanny = cv2.Canny(img, 100, 100) #make it white edges and black bg
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) #increase thickness of whites (edges)
# imgErrosion = cv2.erode(imgDialation,kernel,iterations=1) #decrease the thickness of whites (edges)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Canny Image", imgCanny)
# cv2.imshow("Dialation Image", imgDialation)
# cv2.imshow("Errosion Image", imgErrosion)

# cv2.waitKey(0)

#end of Day 1


