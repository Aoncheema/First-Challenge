import googletrans
import speech_recognition
import gtts
import playsound
input_lang = "hi"
output_lang = "en"

recoginizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("speak now!")
    voice = recoginizer.listen(source)
    text = recoginizer.recognize_google(voice,language = input_lang)
    print(text)
    


translator = googletrans.Translator()
translation = translator.translate(text,dest = output_lang)
print(translation.text)
converted_audio = gtts.gTTS(translation.text,lang = output_lang)
converted_audio.save("hello.mp3")
playsound.playsound("hello.mp3")
