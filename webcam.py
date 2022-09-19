import cv2
import os
import time

while True:

    os.system("rm image.png")

    cam_port = 0
    cam = cv2.VideoCapture(cam_port)

    result, image = cam.read()

    if result:
        cv2.imwrite("image.png", image)
    else:
        print("napaka")

    os.system("git add .")
    os.system("git commit -m 'new image'")
    os.system("git push")
    time.sleep(60)
