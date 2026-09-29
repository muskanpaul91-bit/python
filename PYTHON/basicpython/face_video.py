import cv2
import cv2.data
path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
model =cv2.CascadeClassifier(path)
camera = cv2.VideoCapture(0)
while True:
   status, image = camera.read() 
   faces = model.detectMultiScale(image,1.3,5)
   for oneFace in faces:
        x , y, w, h = oneFace
        image =cv2.rectangle( image,(x,y), (x+w, y+h), (255,255,0), (2))
    
   cv2.imshow("Faces",image)
   if cv2.waitKey(1)== ord('q'):
    break 
   
