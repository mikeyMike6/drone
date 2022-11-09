import Tello

from recognition_and_control.GestureRecognizer import GestureRecognizer
from recognition_and_control.GestureBuffer import GestureBuffer

global drone_battery_status

tello = Tello()
gesture_buffer = GestureBuffer
model = GestureRecognizer()
