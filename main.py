import threading

import cv2
from djitellopy import Tello

from recognition_and_control.GestureBuffer import GestureBuffer
from recognition_and_control.GestureController import GestureController
from recognition_and_control.KeyboardController import KeyboardController
from recognition_and_control.GestureRecognizer import GestureRecognizer


def select_mode(key, mode):
    if key == 110: # n
        mode = 0
    if key == 107: # k - keyboard control
        mode = 1
    if key == 104: # h
        mode = 2
    return mode

def main():
    global gesture_buffer
    global gesture_id
    global battery_status

    keyboard_control = True
    gesture_control = False
    drone_in_air = False

    drone = Tello()
    drone.connect()
    drone.streamon()

    caption = drone.get_frame_read()

    # ---------------controllers and stuff ---------------------
    gesture_controller = GestureController(drone)
    keyboard_controller = KeyboardController(drone)
    gesture_recognition = GestureRecognizer()
    gesture_buffer = GestureBuffer()

    def drone_control(_key, _keyboard_controller, _gesture_controller):

        if keyboard_control:
            keyboard_controller.control(_key)
        else:
            gesture_controller.gesture_control(gesture_buffer)

    def drone_battery(tello):
        global battery_status
        try:
            battery_status = drone.get_battery()[:-2]
        except:
            battery_status = -1

    mode = 0
    battery_status = -1

    while True:
        print('petla true')
        # proccessing keys, esc ends
        key = cv2.waitKey(1) & 0xff
        if key == 27: #esc
            break
        elif key == 32: #space
            if not drone_in_air:
                # takeoff
                drone.takeoff()
                drone_in_air = True
            elif drone_in_air:
                # landing
                drone.land()
                drone_in_air = False
        elif key == ord('k') and gesture_control:
            mode = 0
            keyboard_control = True
            gesture_control = False
            drone.send_rc_control(0, 0, 0, 0)
        elif key == ord('g') and keyboard_control:
            keyboard_control = False
            gesture_control = True

        image = caption.frame
        debug_image, gesture_id = gesture_recognition.recognize_and_draw(image)
        gesture_buffer.add_gesture(gesture_id)
        cv2.imshow("debug_image", debug_image)

        threading.Thread(target=drone_control,
                         args=(key, keyboard_controller, gesture_controller)).start()
        threading.Thread(target=drone_battery, args=(drone,)).start()

if __name__ == "__main__":
    main()