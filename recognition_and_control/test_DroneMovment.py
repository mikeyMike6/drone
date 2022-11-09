from unittest import TestCase


class TestDroneConnection(TestCase):
    def setUp(self):
        self.tello = Tello()
        self.tello.connect()


class TestDroneStreamon(TestDroneConnection):
    def runTest(self):
        self.tello.streamon()

class TestRunDrone(TestDroneConnection):
    def runTest(self):
        move = Move.START
        drone = Drone(self.tello)
        drone.start()
