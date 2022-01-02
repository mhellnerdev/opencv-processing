import cv2

# load image
img = cv2.imread("carina_nebula.tif", 1)

# # print image and debug info
# print(type(img))
# print(img)
# print(img.shape)
# print(img.ndim)

# assign new img variable with resize function applied
resized_image = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

# create gui window to display image for x amount of seconds then destroy
cv2.imshow("carina cordova", resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()