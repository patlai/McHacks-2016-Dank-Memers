import speech_recognition as sr

# obtain audio from the microphone
class Interpreter:
    def __init__(self):
        pass

    def getWords(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        print("Done listening.")
        # recognize speech using Google Speech Recognition
        try:
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # otherwise `r.recognize_google(audio)`
            phrase = r.recognize_google(audio)
            words = phrase.split(" ")
            print("Heard: " + phrase)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return words

    #this part for receiving JSON
    '''
    import json
    receivedJSON = open('textReceived.txt', 'r')
    receivedText = json.loads(receivedJSON.read())
    listOfWords = receivedText['QueryResult']['mrec_results']['transcriptions']
    print(listOfWords[0])
    '''