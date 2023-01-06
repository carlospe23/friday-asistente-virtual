import pyttsx3 as voz
import speech_recognition as sr
import subprocess as sub
from datetime import datetime

#configuracion de la voz del asistente
voice = voz.init()
voices = voice.getProperty('voices')
voice.setProperty('voice',voices[0].id)
voice.setProperty('rate',140)

def say(text):
    voice.say(text)
    voice.runAndWait()

say('Hola Carlos, soy friday, en que te puedo ayudar hoy?')
while True:
    recognizer = sr.Recognizer()
#Activar el microfono
    with sr.Microphone() as source:
        audio = recognizer.listen(source, phrase_time_limit = 3)

    try: #Si se entiende la peticion comenzamos la logica principal
        comando = recognizer.recognize_google(audio, language='es-MX')
        print(f'Creo que dijiiste "{comando}"')

        comando = comando.lower()
        comando = comando.split(' ')

        if 'friday' in comando:
            if 'abre' in comando or 'abrir' in comando:
                sites = {
                    'google': 'google.com',
                    'youtube': 'youtube.com',
                    'instagram': 'instagram.com',
                    'platzi': 'platzi.com'
                }

                for i in list(sites.keys()):
                    if i in comando:
                        sub.call(f'start chrome.exe {sites[i]}', shell=True)
                        say('abriendo {i}')
                    
            elif 'hora' in comando:
                time = datetime.now().strftime('%H:%M')
                say(f'Son las {time}')

            for i in ['termina', 'terminar', 'termino']:
                if i in comando:
                    say('Sesion finalizada')
                    break
            

    except: #Si no se entiende nos dara este mensaje
        say('No te entendi, por favor vuelve a intentarlo')


