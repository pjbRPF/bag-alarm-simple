alarm = 0

def on_gesture_shake():
    global alarm
    alarm = 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global alarm
    alarm = 0
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    if alarm == 1:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SAWTOOTH,
                5000,
                0,
                255,
                255,
                1000,
                SoundExpressionEffect.VIBRATO,
                InterpolationCurve.LINEAR),
            SoundExpressionPlayMode.UNTIL_DONE)
basic.forever(on_forever)
