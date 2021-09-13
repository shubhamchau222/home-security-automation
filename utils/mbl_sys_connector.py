# this file will help to connect mobile cam with the system & provides the images / Videos
# inputs takes the adress of the mobile or cctv for connection 

import cv2

class getVidFromCam:
    def __init__(self , couplingAddress ):
        self.couplingAddress = couplingAddress


    def connect(self):
        capture = cv2.VideoCapture(self.couplingAddress)
        while True : 
            # _ == is there video or not 
            _ , frame = capture.read()
            cv2.imshow('livestream' , frame)
            if cv2.waitKey(1) == ord('q') : 
                break 

        capture.realease()
        cv2.destroyAllwindows()








    