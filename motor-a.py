
from ev3dev2.motor import MediumMotor
from time import sleep
mA = MediumMotor('outA')
mA.reset()


def lift(direction):
    if(direction == "up"):
        mA.run_to_rel_pos(position_sp=130, speed_sp=300, stop_action="coast")
    else:
        mA.run_to_rel_pos(position_sp=-130, speed_sp=300)
    mA.wait_while('running')
