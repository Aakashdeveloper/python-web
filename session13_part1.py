import cv2

face_cascade = cv2.CascadeClassifier("haarcascade.xml")

img = cv2.imread('myimage.jpg')

gray_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05,
minNeighbors=5)

print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)

resized = cv2.resize(img, (int(img.shape[1]/7),int(img.shape[0]/7)))

cv2.imshow('myimage',resized)

cv2.waitKey(0)

cv2.waitTime(2000)
cv2.destroyAllWindows()


'''img = cv2.imread('myimage.jpg',1)
resized = cv2.resize(int(img.shape[1]/2,int(img.shape[0]/2)))
cv2.imshow('myimage',resized)

cv2.waitKey(0)

cv2.waitTime(2000)
cv2.destroyAllWindows()

#print(img.shape)'''