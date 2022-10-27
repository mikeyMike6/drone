import threading
import PySimpleGUI as sg

import cv2
from djitellopy import Tello

from recognition_and_control.GestureBuffer import GestureBuffer
from recognition_and_control.GestureController import GestureController
from recognition_and_control.KeyboardController import KeyboardController
from recognition_and_control.GestureRecognizer import GestureRecognizer

gesture_buffer = GestureBuffer()
gesture_recognition = GestureRecognizer()

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    image, gesture_id, finger_points = gesture_recognition.recognize_and_draw(image)
    gesture_buffer.add_gesture(gesture_id)
    gesture_id = gesture_buffer.get_gesture()
    if gesture_id == 0:
        print(finger_points)
        if finger_points < 0.3:
            gesture_id = 11
        elif finger_points > 0.6:
            gesture_id = 12
        else:
            gesture_id = 6
        image = gesture_recognition.draw_following_info(image)
    image = gesture_recognition.draw_gesture_info(image, gesture_id)
    cv2.imshow("Hands", image)

    key = cv2.waitKey(10)
    if key == 27:  # ESC
        break