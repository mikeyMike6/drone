import unittest
from recognition_and_control.GestureRecognition import GestureRecognition
import cv2
from djitellopy import Tello
from recognition_and_control.Enums.Move import Move
from recognition_and_control.Enums.Gesture import Gesture
from recognition_and_control.DroneMovment import Drone

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = GestureRecognition()
        self.thumbUpImg = cv2.imread(r'C:\python projects\model\thumb_up.jpg')


class TestGestureRecognitonThumbUp(TestModel):
    def runTest(self):
        _, gesture = self.model.recognize_gesture_from(self.thumbUpImg, draw=False)
        self.assertEqual(gesture, Gesture.THUMB_UP)

