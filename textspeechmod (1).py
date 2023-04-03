import PySimpleGUI as sg
import pyttsx3
layout = [
    [sg.Input(key='text'),sg.Button('Speak')],
    [sg.Text('Select Voice Type'),sg.Radio('Male','RADIO',key='-male-',default=True),
     sg.Radio('Female','RADIO',key='-female-')],
    [sg.Text('Volume:'),sg.Text('Speed:',pad=(150,0))],
    [sg.Slider(range=(0,10),default_value=5,orientation='h',size=(20,15),key='-VOLUME-'),
     sg.Slider(range=(0,10),default_value=10,orientation='h',size=(20,15),key='-SPEED-')]
]

window =sg.Window('Text to Speech App',layout)

while True:
    event,values = window.read()
    engine = pyttsx3.init()
    
    if event== sg.WIN_CLOSED:
        break
    elif event == 'Speak':
        voices = engine.getProperty('voices') 
        speed = engine.getProperty('rate')
        volume = engine.getProperty('volume')   

        text = values['text']
        speed_value = (values['-SPEED-']*20)
        volume_value = (values['-VOLUME-']/10)

        engine.setProperty('rate',speed_value)
        engine.setProperty('volume',volume_value)

        if values['-male-']:
           engine.setProperty('voice', voices[0].id)
        else:
           engine.setProperty('voice', voices[1].id)
        
        engine.say(text)
        engine.runAndWait()
        
window.close()

