import speech_recognition as sr

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

def here():
    print('here')

def check_speech_and_dispense(mic, recognizer, keyphrase):
    result = recognize_from_mic(mic, recognizer)

    # we check if the keyphrase is in the result (that way there can be background noise and other words can accidentally get picked up)
    if keyphrase in result:
        print('Keyphrase is correct, dispensing alcohol!')

if __name__ == '__main__':
    # phrase that needs to be heard in order to dispense a drink
    keyphrase = 'drink please'
    microphone_name = 'Blue Snowball: USB Audio (hw:1,0)'

    # initialize speech recognizer and microphone instances
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index = sr.Microphone.list_microphone_names().index(microphone_name))    

    check_speech_and_dispense(mic, recognizer, keyphrase)
    
    # while True:
    #     keyboard.on_press_key('f', lambda  mic=mic, recognizer=recognizer, keyphrase=keyphrase: check_speech_and_dispense)

