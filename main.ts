input.onButtonPressed(Button.A, function on_button_pressed_a() {
    MotorDriver.MotorRun(Motor.A, Dir.forward, 16)
    MotorDriver.MotorRun(Motor.B, Dir.forward, 16)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    MotorDriver.MotorRun(Motor.A, Dir.backward, 16)
    MotorDriver.MotorRun(Motor.B, Dir.backward, 16)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    MotorDriver.MotorRun(Motor.A, Dir.forward, 16)
    MotorDriver.MotorRun(Motor.B, Dir.backward, 16)
})
pins.setPull(DigitalPin.P0, PinPullMode.PullUp)
pins.setPull(DigitalPin.P1, PinPullMode.PullUp)
pins.setPull(DigitalPin.P2, PinPullMode.PullUp)
basic.forever(function on_forever() {
    if (pins.digitalReadPin(DigitalPin.P0) == 0) {
        MotorDriver.MotorRun(Motor.A, Dir.backward, 10)
        MotorDriver.MotorRun(Motor.B, Dir.forward, 10)
    } else if (pins.digitalReadPin(DigitalPin.P1) == 0) {
        MotorDriver.MotorRun(Motor.B, Dir.backward, 10)
        MotorDriver.MotorRun(Motor.A, Dir.backward, 10)
        basic.pause(1000)
        MotorDriver.MotorRun(Motor.A, Dir.backward, 10)
        MotorDriver.MotorRun(Motor.B, Dir.forward, 10)
    } else if (pins.digitalReadPin(DigitalPin.P2) == 0) {
        MotorDriver.MotorRun(Motor.A, Dir.forward, 10)
        MotorDriver.MotorRun(Motor.B, Dir.backward, 10)
    } else {
        MotorDriver.MotorRun(Motor.A, Dir.forward, 10)
        MotorDriver.MotorRun(Motor.B, Dir.forward, 10)
    }
    
})
