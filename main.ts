let alarm = 0
input.onGesture(Gesture.Shake, function () {
    alarm = 1
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    alarm = 0
})
basic.forever(function () {
    if (alarm == 1) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Sawtooth, 5000, 0, 255, 255, 1000, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    }
})
