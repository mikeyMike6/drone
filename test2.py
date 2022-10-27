from djitellopy import Tello
import cv2, math, time
import threading

from recognition_and_control.GestureBuffer import GestureBuffer
from recognition_and_control.GestureController import GestureController
from recognition_and_control.GestureRecognizer import GestureRecognizer

# zmienne globalne
from recognition_and_control.KeyboardController import KeyboardController

global battery_status

# inicjacja modułów

tello = Tello()
gesture_buffer = GestureBuffer()
gesture_recognizer = GestureRecognizer()
keyboard_control = KeyboardController(tello)
gesture_control = GestureController(tello)

# połączenie z dronem i kamerą
tello.connect()
tello.streamon()
frame_read = tello.get_frame_read()

# zmienne
height, width, _ = frame_read.frame.shape
drone_in_following_mode = False
drone_in_gesture_control = True

video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))


def dron_control(_key,  _gesture_id):
    gesture_control.gesture_control(_gesture_id)


def dron_battery_info():
    global battery_status
    try:
        battery_status = tello.get_battery()
    except:
        battery_status = -1


while True:

    threading.Thread(target=dron_battery_info, args=()).start()
    key = cv2.waitKey(1) & 0xff
    if key == 27:  # ESC
        break
    img = frame_read.frame
    img, gesture_id, finger_points = gesture_recognizer.recognize_and_draw(img)
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
        img = gesture_recognizer.draw_following_info(img)
    img = gesture_recognizer.draw_gesture_info(img, gesture_id)
    img = cv2.putText(img, str(battery_status), (700, 700),
                      cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 1, cv2.LINE_AA)
    threading.Thread(target=dron_control, args=(key, gesture_id,)).start()
    video.write(img)
    cv2.imshow("drone", img)

tello.land()
video.release()