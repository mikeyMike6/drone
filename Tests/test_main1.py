from recognition_and_control.GestureRecognizer import GestureRecognizer
import cv2

gesture_rec = GestureRecognizer()


def test_gesture_recognition():
    image = cv2.imread(r'C:\python projects\Tests\open_hand.jpg')
    expected_gesture_id = 4
    _, gesture_id, _ = gesture_rec.recognize_and_draw(image)
    assert gesture_id == expected_gesture_id
