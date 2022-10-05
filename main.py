def on_button_pressed_a():
    MotorDriver.motor_run(Motor.A, Dir.FORWARD, 16)
    MotorDriver.motor_run(Motor.B, Dir.FORWARD, 16)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    MotorDriver.motor_run(Motor.A, Dir.BACKWARD, 16)
    MotorDriver.motor_run(Motor.B, Dir.BACKWARD, 16)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    MotorDriver.motor_run(Motor.A, Dir.FORWARD, 16)
    MotorDriver.motor_run(Motor.B, Dir.BACKWARD, 16)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

pins.set_pull(DigitalPin.P0, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P1, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P2, PinPullMode.PULL_UP)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P0) == 0:
        MotorDriver.motor_run(Motor.A, Dir.BACKWARD, 10)
        MotorDriver.motor_run(Motor.B, Dir.FORWARD, 10)
    elif pins.digital_read_pin(DigitalPin.P1) == 0:
        MotorDriver.motor_run(Motor.B, Dir.BACKWARD, 10)
        MotorDriver.motor_run(Motor.A, Dir.BACKWARD, 10)
        basic.pause(1000)
        MotorDriver.motor_run(Motor.A, Dir.BACKWARD, 10)
        MotorDriver.motor_run(Motor.B, Dir.FORWARD, 10)
    elif pins.digital_read_pin(DigitalPin.P2) == 0:
        MotorDriver.motor_run(Motor.A, Dir.FORWARD, 10)
        MotorDriver.motor_run(Motor.B, Dir.BACKWARD, 10)
    else:
        MotorDriver.motor_run(Motor.A, Dir.FORWARD, 10)
        MotorDriver.motor_run(Motor.B, Dir.FORWARD, 10)
basic.forever(on_forever)
