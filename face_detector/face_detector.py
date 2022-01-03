import cv2

# call CascadeClassifier Function on xml model
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# store image
img = cv2.imread("news.jpg")

# store grayscale version of image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# create object variable of faces that have been detected with passed in function
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

for x, y, w, h, in faces:
  img = cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 3)

# debug info. prints cordinates of faces into arrays. numpy array.
print(type(faces))
print(faces)

# resize image output by half original size
resized = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))


# show window with rezised image passed in
cv2.imshow("Gray Image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
