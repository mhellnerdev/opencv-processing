import cv2
import glob

images = glob.glob("*.tif")


# resize all images found in local folder to 100x100px
for image in images:
  img = cv2.imread(image, 1)
  re = cv2.resize(img, (100, 100))
  cv2.imshow("Rezided", re)
  cv2.waitKey(500)
  cv2.destroyAllWindows()
  cv2.imwrite("resized_" + image, re)