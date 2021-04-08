import cv2
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('/home/achintya/Downloads/haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    
    if ret:
        faces = face_cascade.detectMultiScale(frame)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            roi_color = frame[y:y+h, x:x+w]

        cv2.imshow("My Window", frame)
    
    key = cv2.waitKey(1)
   

    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()