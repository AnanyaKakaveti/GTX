import keyboard
from google.cloud import speech

import pyaudio
import wave
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"   ###PUT YOUR MANAGER JSON IN MAIN


def MakeUserFile():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1  # Mono
    RATE = 44100  # Sample rate (samples per second)
    RECORD_SECONDS = 5  # Duration of recording in seconds

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Set up the audio stream
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=1024)

    print("Recording...")

    frames = []

    # Record audio

    while(not keyboard.is_pressed(' ')):
        data = stream.read(1024)
        frames.append(data)


# for _ in range(0, int(RATE / 1024 * RECORD_SECONDS)):
#        data = stream.read(1024)
#        frames.append(data)

    print("Finished recording")

    # Stop and close the audio stream
    stream.stop_stream()
    stream.close()

    # Terminate PyAudio
    audio.terminate()

    # Save the recorded audio to a file
    with wave.open("Input.mp3", 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved as Input.mp3")


def GetUserInput(trueLine):             #be sure this file is download as input.mp3

    client = speech.SpeechClient.from_service_account_json('key.json')

    MakeUserFile()

    fileName = "Input.mp3"

    with open(fileName, 'rb') as f:
        mp3d = f.read()

    audio_file = speech.RecognitionAudio(content = mp3d)

    config = speech.RecognitionConfig(sample_rate_hertz = 44100,
                                  enable_automatic_punctuation = False,
                                  language_code= 'es-MX')

    response = client.recognize(config=config, audio=audio_file)
    userSays = response.results[0].alternatives[0].transcript
    print(userSays)
    wordsInResponse = userSays.split()
    wordsInTrue = trueLine.split()
    percentage = GetPercentage(wordsInResponse, wordsInTrue)
    print(f"you got {percentage}% correct!!!")
    if wordsInTrue != wordsInResponse:
        print("Did you say all the words?")

    return percentage



   #     print(userSays)  # Print the transcript


def GetPercentage(wordsInResponse, wordsInTrue):
    correct = 0
    i = 0
    print(wordsInResponse)
    print(wordsInTrue)
    for j in range(len(wordsInResponse)):
        if(wordsInTrue[i] == wordsInResponse[j]):
            correct += 1
        elif(i != len(wordsInTrue) - 1 and wordsInTrue[i + 1] == wordsInResponse[j]):
             i += 1
        elif(wordsInTrue[i -1] == wordsInResponse[j]):
             i -=1

        i += 1
        if(i == len(wordsInTrue)):
            break                       #emergency break to prevent a seg fault

    return (correct / len(wordsInTrue)) * 100



#GetUserInput("yes")

# trueLine = "suerte que en el sur hayas nacido"

"""
developerResp = int(input("Record(1) or Test(2)?"))
if(developerResp == 1):
    print("c")
    MakeUserFile()
elif(developerResp == 2):
    GetUserInput(trueLine)
"""