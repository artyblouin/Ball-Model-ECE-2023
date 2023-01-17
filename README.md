# Ball-Model-ECE-2023
Speech Recognition Script for the 2023 E-Week Ball model for Electrical and Computer Engineering

## Set up

In order to run this script we use a library called SpeechRecognition. In order to use microphone inputs, this package depends on another library called PyAudio. These two packages need to be installed in order for the script to run. 

To install SpeechRecognition: 
```pip install SpeechRecognition```

To install PyAudio on a debian based system:
```sudo apt-get install python-pyaudio python3-pyaudio```

If that does not work use the following command instead:
```sudo apt-get install portaudio19-dev python-all-dev python3-all-dev```

Then Run:
```pip install PyAudio```

For more information on setup you can visit SpeechRecognition's github [here](https://github.com/Uberi/speech_recognition?undefined)

## Wiring

PIN 17 is configured as the input pin for the button used for audio recording. Yellow - Yellow cable

PIN 22 is confgured as the PWM pin for driving the mosfet controllers of our motors. Green - Yellow cable

PIN 1 is 3.3v DC. Blue - green cable

PIN 26 is ground. White - Brown cable

If the motors are wired forward, the output is on the left side of the pump.


