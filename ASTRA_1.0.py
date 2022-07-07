import speech_recognition as reconocimientoVoz
import pyttsx3
import pywhatkit
import json
import datetime

listener=reconocimientoVoz.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

name='Alexa'

def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

def escuchar():
    try:
        with reconocimientoVoz.Microphone() as fuente:
            print("Escuchando...")
            voice=listener.listen(fuente)
            rec=listener.recognize_google(voice)
            rec=rec.lower()
            print(rec)
            if name in rec:
                hablar('Dime... ¿En qué te puedo ayudar?')
            # else:
            #     hablar('Disculpa, no reconozco tu instrucción.')
    except:
        pass
    return rec

def reproducirYoutube():
    rec=escuchar()
    if 'reproduce' in rec:
        music=rec.replace('reproduce','')
        hablar('Reproduciendo ' +music)
        pywhatkit.playonyt(music)

#reproducirYoutube()

def darHoraActual():
    rec=escuchar()
    if 'hora' in rec:
        horaActual=datetime.datetime.now().strftime('%I:%M %p')
        hablar('Son las '+horaActual)

# darHoraActual()