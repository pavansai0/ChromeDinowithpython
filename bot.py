import time
import pyautogui
import cv2
import mss
import numpy

time.sleep(2)

def check(img):
    for i in range(650, 690):
            for j in range(320,420):
                if(img[i,j]>120):
                    pyautogui.press('up') 
                    return
                


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 0, "left": 0, "width": 3000, "height": 3000}

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))
        img= cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

        check(img)
        # for i in range(650, 690):
        #     for j in range(320,420):
        #         img[i,j]=120
                    
        for i in range(650, 690):
            for j in range(320,420):
                if(img[i,j]>120):
                    pyautogui.press('up') 
                    break
                
                    
        

       # Display the picture
        # cv2.imshow("OpenCV/Numpy normal", img)
        # cv2.waitKey(0)         

        #print("fps: {}".format(1 / (time.time() - last_time)))

        # Press "q" to quit
        #if cv2.waitKey(25) & 0xFF == ord("q"):
        #    cv2.destroyAllWindows()
        #    break

        # for i in range(650, 690):
        #     for j in range(320,420):
        #         if(img[i,j]>120):
        #             pyautogui.press('up')
