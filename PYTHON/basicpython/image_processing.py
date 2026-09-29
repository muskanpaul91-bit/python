import cv2
image = cv2.imread("gill.jpg")
cv2.imshow("Frame",image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Frame",gray_image)
cv2.waitKey(0)

import cv2
image = cv2.imread("gill.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # black and white
cv2.imshow("GILL",image)
cv2.imshow("Frame",gray_image)
cv2.waitKey(0)

# import cv2
# image = cv2.imread("gill.jpg")
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # black and white
# blue_image = cv2.cvtColor(image ,cv2.COLOR_BGR2RGBA )
# cv2.imshow("Frame",image)
# cv2.waitKey(1000)
# cv2.imshow("Frame",gray_image)
# cv2.waitKey(1000)
# cv2.imshow("Frame",blue_image)
# cv2.waitKey(1000)

# rec =cv2.rectangle( image,(100,120), (180, 210), (255,255,0), (1))
# cv2.imshow("Frame",rec)
# cv2.waitKey(0)






# print(image.ndim)
# print(image.shape)


