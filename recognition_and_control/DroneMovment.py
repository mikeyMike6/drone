from djitellopy import Tello
from recognition_and_control.Enums.Move import Move

class Drone:
    def __init__(self, tello: Tello):
        self.in_air = False
        self.tello = tello
        self.forw_back_velocity = 0
        self.up_down_velocity = 0
        self.left_right_velocity = 0
        self.yaw_velocity = 0
        self.speed = 30

    def start(self):
        self.forw_back_velocity = 0
        self.up_down_velocity = 0
        self.left_right_velocity = 0
        self.yaw_velocity = 0
        self.tello.takeoff()
        self.in_air = True

    def land(self):
        self.in_air = False
        self.forw_back_velocity = 0
        self.up_down_velocity = 0
        self.left_right_velocity = 0
        self.yaw_velocity = 0
        self.tello.land()

    def forward(self):
        self.forw_back_velocity = self.speed

    def stop(self):
        self.forw_back_velocity = 0
        self.up_down_velocity = 0
        self.left_right_velocity = 0
        self.yaw_velocity = 0

    def back(self):
        self.forw_back_velocity = -self.speed

    def left(self):
        self.left_right_velocity = self.speed

    def right(self):
        self.left_right_velocity = -self.speed

    def up(self):
        self.up_down_velocity = self.speed

    def down(self):
        self.up_down_velocity = -self.speed

    def left_turn(self):
        self.yaw_velocity = self.speed

    def right_turn(self):
        self.yaw_velocity = -self.speed

    def movement(self, move: Move):
        if move != move.NONE:
            if self.in_air:
                if move == Move.STOP:
                    self.stop()
                if move == Move.LAND:
                    self.land()
            if not self.in_air:
                if move == Move.START:
                    self.start()
        else:
            self.stop()
        self.tello.send_rc_control(self.left_right_velocity, self.forw_back_velocity,
                                   self.up_down_velocity, self.yaw_velocity)
