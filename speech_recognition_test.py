import speech_recognition as sr
from gpiozero import Button, PWMOutputDevice
import time

def recognize_from_mic(mic, recognizer):

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print('Audio Recording Started!')
        audio = recognizer.listen(source, phrase_time_limit=3)
        print('Audio Recording Complete!')

    try:
        transcript = recognizer.recognize_google(audio)
    except:
        print('Failed to recognize speech, returning empty string')
        transcript = ''

    return transcript

def check_speech_and_dispense(mic, recognizer, keyphrase):
    result = recognize_from_mic(mic, recognizer)

    # we check if the keyphrase is in the result (that way there can be background noise and other words can accidentally get picked up)
    if keyphrase in result:
        print('Keyphrase is correct, dispensing alcohol!')
        return True
    else: 
        return False


if __name__ == '__main__':
    # phrase that needs to be heard in order to dispense a drink
    keyphrase = 'drink please'
    microphone_name = 'Blue Snowball: USB Audio (hw:1,0)'

    # GIO Configuration
    RECORD_BUTTON_PIN = 17
    MOTOR_PWM_PIN = 22
    frequency = 1000

    button = Button(RECORD_BUTTON_PIN)
    motor_pwm = PWMOutputDevice(MOTOR_PWM_PIN, frequency=1000, initial_value=1)

    # initialize speech recognizer and microphone instances
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index = sr.Microphone.list_microphone_names().index(microphone_name))    

    while True:
        if not button.is_pressed:
            if check_speech_and_dispense(mic, recognizer, keyphrase):
                motor_pwm.value = 0
                time.sleep(10)
                motor_pwm.value = 1

