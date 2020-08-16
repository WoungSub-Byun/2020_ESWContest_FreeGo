def voice_recognize():
    import pyaudio
    import wave
    import keyboard
    import speech_recognition as sr
    import array

    FORMAT = pyaudio.paInt16
    CHANNELS = 1 #change this to what your sound card supports
    #input_device_index => change this your input sound card index
    RATE = 16000
    CHUNK = 1024
    WAVE_OUTPUT_FILENAME = "file.wav"

    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16,
                       channels = CHANNELS,
                       rate = RATE,
                       input = True,output = False,
                       input_device_index = 0,
                       frames_per_buffer=CHUNK)
    while True:
        try:
            print("recording................")
            
            frames = []

            while True:
                if keyboard.is_pressed("s"):
                    print('s pressed...')
                    while not keyboard.is_pressed("q"):
                        data = stream.read(CHUNK, exception_on_overflow = False)
                        frames.append(data)
                    break

            stream.stop_stream()
            stream.close()
            audio.terminate()
            waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            waveFile.setnchannels(CHANNELS)
            waveFile.setsampwidth(audio.get_sample_size(FORMAT))
            waveFile.setframerate(RATE)
            waveFile.writeframes(b''.join(frames))
            waveFile.close()
            r = sr.Recognizer()
            harvard = sr.AudioFile('file.wav')
            with harvard as source:
                audio = r.record(source)
                
            return r.recognize_google(audio, language='ko-KR')

        except Exception as err:
            print("Error Log : [{}]".format(err))   
            return "fail"


def runSpeechRecognizer(id):
    from tts import speech
    import requests
    import crawling

    msg = voice_recognize()
    msg = msg.replace(" ","")
    print("input message: [{}]".format(msg))

    if msg == "목록보여줘":
        speech("알겠습니다")
        body = {'id' : id}
        res = requests.post('13.125.244.112:5000/show', data=body)
        return res

    elif "요리알려줘" in msg:
        speech("알겠습니다")
        msg = msg.replace("요리알려줘","")
        res = crawling.find_reciepe(msg)
        return res

    elif "있어" in msg:
        speech("찾아볼게요")
        msg = msg.replace("있어","")
        body = {'id' : id, 'p_name' : msg }
        res = requests.post('13.125.244.112:5000/find', data=body)
        return res
    else:
        speech("인식하지 못했습니다.")
        return "fail"


# 음성인식모드 실행
# -
# ```
#     GET /speech
# ```
# - Request
# ```
# ```
# - Response
# ```
#     SUCCESS { "code": 200,
#             "data": [
#                 {
#                 "ex_date": "Mon, 31 Aug 2020 00:00:00 GMT",
#                 "name": "가지",
#                 "number": 4
#                 }, ...
#             ],
#             "message" : "success"
#     }

#     SUCCESS { "code": 200,
#             "data": {
#                 "[요리제목0]" : "[레시피 설명 링크0]",
#                 "[요리제목1]" : "[레시피 설명 링크1]",
#                 "[요리제목2]" : "[레시피 설명 링크2]",
#                 ...
#                 },
#             "message" : "success"
#      }

#     FAIL { "code": 404, "message": "fail" }
# ```