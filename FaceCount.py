import numpy as np
import cv2
import tkinter as tk
import tkinter.messagebox as tkMessageBox


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_faces(img,cascade):
	gray_frame = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = cascade.detectMultiScale(gray_frame,1.1,5)
	print("Found {0} faces!",format(len(faces)))
	
	if len(faces) >= 2:
		root = tk.Tk()
		root.withdraw()
		#tkMessageBox.showwarning('Alert','Someone is watching')
		#cv2.putText(gray_frame, "SOMEONE IS WATCHING", cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
		cv2.putText(gray_frame, 'SOMEONE IS WATCHING', (50,50), cv2.FONT_HERSHEY_SIMPLEX,  
                   1, (255,0,0), 2, cv2.LINE_AA) 
		cv2.imshow('Alert',gray_frame)

	return faces


def main():
	cap = cv2.VideoCapture(0)
	cv2.namedWindow('Faces')
	 
	while True:
		rval,frame = cap.read()
		faces = detect_faces(frame,face_cascade)

		for (x,y,w,h) in faces:
			cv2.rectangle(frame,(x,y),(x+w,y+h), (0, 255,0),2)
		
		cv2.imshow('Faces',frame)
		key = cv2.waitKey(20)
		
		if key == 27:
			break
	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
