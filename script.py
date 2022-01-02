import cv2


img = cv2.imread("carina_nebula.tif", 1)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image = cv2.resize(img, (1920, 1080))

cv2.imshow("carina cordova", resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()