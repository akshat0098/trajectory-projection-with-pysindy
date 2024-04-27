
# Python program to illustrate  
# saving an operated video 
  
# organize imports 
import numpy as np 
import cv2 
from uuid import uuid4


BASE_FOLDER_DIR = 'video'

def record():
    # This will return video from the first webcam on your computer. 
    cap = cv2.VideoCapture(0)   
    recording_filename = uuid4()

    # Define the codec and create VideoWriter object 
    fourcc = cv2.VideoWriter_fourcc(*'XVID') #(*'MP4V') 
    out = cv2.VideoWriter(f'video/{recording_filename}.avi', fourcc, 30.0, (640, 480)) 
    
    # loop runs if capturing has been initialized.  
    while(True): 
        # reads frames from a camera  
        # ret checks return at each frame 
        ret, frame = cap.read()  
    
        # Converts to HSV color space, OCV reads colors as BGR 
        # frame is converted to hsv 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
        
        # output the frame 
        out.write(frame)  
        
        # The original input frame is shown in the window  
        cv2.imshow('Original', frame) 
    
        # The window showing the operated video stream  
        cv2.imshow('frame', hsv) 
    
        # Wait for 'a' key to stop the program  
        if cv2.waitKey(1) & 0xFF == ord('a'): 
            break
    
    print(f"video/{recording_filename}.avi is saved")


    # Close the window / Release webcam 
    cap.release() 
    
    # After we release our webcam, we also release the output 
    out.release()  
    

    # De-allocate any associated memory usage  
    cv2.destroyAllWindows() 


if __name__ == "__main__":
    record()