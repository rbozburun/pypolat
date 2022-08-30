import speech_recognition as sr
from playsound import playsound

class Polat():
    def __init__(self):
        self.isSpoke = False
        self.isExit = False
        pass

    def record(self):
        vr = sr.Recognizer()
        print("Dinliyorum...")
        
        with sr.Microphone() as source:
            m_audio = vr.listen(source)
            voice = ""

            try: 
                voice = vr.recognize_google(m_audio, language='tr-TR')

            except sr.UnknownValueError:
                print("Anlamadım...")

            except sr.RequestError:
                print("Sisteme erişilemiyor... Internet bağlantını kontrol et.")

            return voice


    def speak(self, voice):
        self.isSpoke = not self.isSpoke
        voice = voice.lower()
        print(voice)

        if "orada mısın" in voice:
            playsound("./voices/evet-memati.mp3")
            return

        elif "ölüm" in voice:
            playsound("./voices/olum-olum-dedigin-nedir-ki-gulum.mp3")
            return

        elif "eyvallah" in voice:
            playsound("./voices/eyvallah.mp3")
            self.isExit = not self.isExit
            return

        elif "taksi" in voice:
            playsound("./voices/kacak-taksicilik-isinde-cok-para-varmis-memati.mp3")
            return

        elif "uyku" in voice:
            playsound("./voices/sen-benim-geceleri-uyudugumu-mu-saniyosun-memati.mp3")
            return

        elif "mutlu olurum" in voice:
            playsound("./voices/sen-mutlu-olmaya-devam-et-yedi-tepeye-gomerim.mp3")
            return

        elif "sonumuz" in voice:
            playsound("./voices/sonunu-dusunen-kahraman-olamaz.mp3")
            return

        elif "aynı yoldayız" in voice:
            playsound("./voices/dostun-dostumdur-dusmanin-dusmanim.mp3")
            return   

             



polat = Polat()

while True:
    while polat.isExit == False:
        voice = polat.record()
        polat.speak(voice)
        polat.isSpoke = not polat.isSpoke
        voice = ""

    break




