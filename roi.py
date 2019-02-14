import cv2
im = cv2.imread('test.jpg')
imgray = cv2.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for i in range(0,len(contours)):
     x, y, width, height = cv2.boundingRect(contours[i])
     roi = img[y:y+height, x:x+width]
     cv2.imwrite("roi%d.png", i)

