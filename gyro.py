from ev3dev2.sensor.lego import GyroSensor

gy = GyroSensor()

gy.mode = GyroSensor.MODE_TILT_ANG
gy.reset()


def is_in_angle():
    gy.mode = GyroSensor.MODE_TILT_ANG
    return abs(gy.tilt_angle) > 2
