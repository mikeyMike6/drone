import cv2

from recognition_and_control.GestureBuffer import GestureBuffer
from recognition_and_control.GestureRecognizer import GestureRecognizer

gesture_buffer = GestureBuffer()
gesture_recognition = GestureRecognizer()

cap = cv2.VideoCapture(0)


def show():
    success, image = cap.read()
    image, gesture_id = gesture_recognition.recognize_and_draw(image)
    gesture_buffer.add_gesture(gesture_id)
    gesture_id = gesture_buffer.get_gesture()
    print(gesture_id)
    image = gesture_recognition.draw_gesture_info(image, gesture_id)
    cv2.imshow("Hands", image)

    key = cv2.waitKey(10)
    if key == 27:  # ESC
        return True


while True:
    breakLoop = show()
    if breakLoop:
        break
