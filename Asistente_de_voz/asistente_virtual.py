import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id4 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'


def trasformar_audio_en_texto():

    r = sr.Recognizer()

    with sr.Microphone() as origen:

        r.pause_threshold = 0.8

        print("ya puedes hablar")

        audio = r.listen(origen)

        try:
   
            pedido = r.recognize_google(audio, language="es-ar")

            print("Dijiste: " + pedido)

            return pedido

        except sr.UnknownValueError:

            print("ups, no entendi")

            return "sigo esperando"

        except sr.RequestError:

            print("ups, no hay servicio")

            return "sigo esperando"

        except:

            print("ups, algo ha salido mal")

            return "sigo esperando"