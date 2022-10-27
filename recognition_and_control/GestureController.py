from djitellopy import Tello


class GestureController:
    def __init__(self, tello: Tello):
        self.tello = tello
        self.is_landing = False
        self.in_air = False

        self.forw_back_velocity = 0
        self.up_down_velocity = 0
        self.left_right_velocity = 0
        self.yaw_velocity = 0
        self.speed = 30

    def gesture_control(self, gesture_id):
        print(gesture_id)
        if gesture_id != -1:
            print(gesture_id)
        if not self.in_air:
            if gesture_id == 5: # start
                self.in_air = True
                self.forw_back_velocity = 0
                self.up_down_velocity = 0
                self.left_right_velocity = 0
                self.yaw_velocity = 0
                self.tello.takeoff()
        if self.in_air:
            if gesture_id == 9: # lądowanie
                self.in_air = False
                self.forw_back_velocity = 0
                self.up_down_velocity = 0
                self.left_right_velocity = 0
                self.yaw_velocity = 0
                self.tello.land()
            if gesture_id == 4: # do przodu
                self.forw_back_velocity = self.speed
            elif gesture_id == 6 or gesture_id == -1: # stop
                self.forw_back_velocity = 0
                self.up_down_velocity = 0
                self.left_right_velocity = 0
                self.yaw_velocity = 0
            if gesture_id == 3: # do tylu
                self.forw_back_velocity = -self.speed
            if gesture_id == 7: # w moje lewo
                self.left_right_velocity = self.speed
            elif gesture_id == 8: # w moje prawo
                self.left_right_velocity = -self.speed
            if gesture_id == 1: # w gore
                self.up_down_velocity = self.speed
            elif gesture_id == 2: # w dol
                self.up_down_velocity = -self.speed
            elif gesture_id == 11:  # obrót w lewo
                self.yaw_velocity = self.speed
            elif gesture_id == 12:  # obrót w prawo
                self.yaw_velocity = -self.speed
            self.tello.send_rc_control(self.left_right_velocity,
                                       self.forw_back_velocity,
                                       self.up_down_velocity,
                                       self.yaw_velocity)
