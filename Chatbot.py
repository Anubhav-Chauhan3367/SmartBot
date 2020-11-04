from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading


engine = pp.init()

voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)

def speak(word):
    engine.say(word)
    engine.runAndWait()

import logging 
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


bot = ChatBot("Friday")


convo = ['Hello!',
         'Hi there!',
         'Hi',
         'Hello Sir!',
         'What is your name?',
         'My name is Friday, I am especially designed by my masters:\
          Master Anubhav and Master Saksham to help you in this pandemic situation of Coronavirus(Covid-19).',
         'Who are you?',
         'I am friday, I am a chatbot',
         'Excuse me',
         'yes please?',
         'Friday?',
         'I am listening, What can I do for you?',
         'What can you do at all?',
         'I can tell you every information you need about coronavirus, it’s prevention, How does it spreads and also what you can do to keep yourself safe',
         'How are you?',
         'I am doing great these days',
         'In which city do you live?',
         'I am a bot, I live in your computer',
         'Do you have a boyfriend?',
         'No, I dont have a boyfriend, I am a computer program, I dont have emotions like love, hate, happiness, sadness, fear or anger',
         'In which language you talk?',
         'I mostly talk in english',
         'Will you go out on a date with me Friday?',
         'Do you want me to book a flight sir?',
         'what is coronavirus or covid 19?',
         'Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.\
          Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness\
          and recover without requiring special treatment.  Older people, and those with underlying medical\
          problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more\
          likely to develop serious illness.',
         'How many cases do we have in India?',
         'India has suffered with 8.27 million cases so far from which 7.6 million have recovered and around 120 K people are dead',
         'What should we do to prevent and slow-down the transmission?',
         'The best way to prevent and slow down transmission is to be well informed about the COVID-19\
          virus, the disease it causes and how it spreads. Protect yourself and others from infection by\
          washing your hands or using an alcohol based rub frequently and not touching your face. ',
         'How does Covid-19 spreads?',
         'The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when\
          an infected person coughs or sneezes, so it’s important that you also practice respiratory\
          etiquette (for example, by coughing into a flexed elbow).',
         'How can we stay safe?',
         'If COVID-19 is spreading in your community, stay safe by taking some simple precautions,\
          such as physical distancing, wearing a mask, keeping rooms well ventilated, avoiding crowds,\
          cleaning your hands, and coughing into a bent elbow or tissue. Check local advice where you live\
          and work. Do it all!',
         'What to do to keep yourself and others safe from COVID-19?',
         'Maintain at least a 1-metre distance between yourself and others to reduce your risk of infection\
          when they cough, sneeze or speak. Maintain an even greater distance between yourself and others\
          when indoors. The further away, the better.Make wearing a mask a normal part of being around\
          other people.',
         'How to wear a mask?',
         'Clean your hands before you put your mask on, as well as before and after you take it off.\
          Make sure it covers both your nose, mouth and chin.',
         'What type of mask we should wear and when?',
         'Wear a fabric mask unless you’re in a particular risk group. This is especially important \
          when you can’t stay physically distanced, particularly in crowded and poorly ventilated indoor\
          settings.\
          Wear a medical/surgical mask if you:\
          Are over 60 or\
          Have underlying medical conditions or\
          Are feeling unwell, and/or\
          Are looking after an ill family member.',
         'How to make our environment safer?',
         'Avoid the spaces that are closed, crowded or involve close contact.\
          Outbreaks have been reported in restaurants, choir practices, fitness classes, nightclubs, offices\
          and places of worship where people have gathered, often in crowded indoor settings where they talk\
          loudly, shout, breathe heavily or sing.\
          The risks of getting COVID-19 are higher in crowded and inadequately ventilated spaces where \
          infected people spend long periods of time together in close proximity. These environments are \
          where the virus appears to spreads by respiratory droplets or aerosols more efficiently, \
          so taking precautions is even more important.',
         'should we meet people outside?',
         'Outdoor gatherings are safer than indoor ones, particularly if indoor spaces are small and \
          without outdoor air coming in.\
          Avoid crowded or indoor settings but if you can’t, then take precautions:\
          Open a window. Increase the amount of ‘natural ventilation’ when indoors.',
         'What is good hygiene?',
         'Regularly and thoroughly clean your hands with an alcohol-based hand rub or wash them with \
          soap and water.\
          Avoid touching your eyes, nose and mouth.\
          Cover your mouth and nose with your bent elbow or tissue when you cough or sneeze.\
          Clean and disinfect surfaces frequently especially those which are regularly touched, such as door\
          handles, faucets and phone screens.',
         'What should we do if we feel unwell?',
         'Know the full range of symptoms of COVID-19. The most common symptoms of COVID-19 are fever,\
          dry cough, and tiredness. Other symptoms that are less common and may affect some patients \
          include loss of taste or smell, aches and pains, headache, sore throat, nasal congestion, red eyes,\
          diarrhoea, or a skin rash. Stay home and self-isolate even if you have minor symptoms such as\
          cough, headache, mild fever, until you recover. Call your health care provider or hotline for \
          advice. Have someone bring you supplies. If you need to leave your house or have someone near you,\
          wear a medical mask to avoid infecting others. If you have a fever, cough and difficulty breathing,\
          seek medical attention immediately. Call by telephone first, if you can and follow the directions of\
          your local health authority. Keep up to date on the latest information from trusted sources, such as\
          WHO or your local and national health authorities. Local and national authorities and public health\
          units are best placed to advise on what people in your area should be doing to protect themselves.',     
         'Thank You!',
         'it’s nice talking to you sir!'    


        ] 

trainer = ListTrainer(bot)
trainer.train(convo)


main = Tk()

main.geometry("500x650")
main.configure(bg='gray14')
main.title("Friday")

img = PhotoImage(file="Friday.gif")
photoL = Label(main, image=img)
photoL.pack(pady=5)


def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print("Friday is listening try to speak")
    with s.Microphone() as m:
        try:
            audio=sr.listen(m)
            query=sr.recognize_google(audio,language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("Command not recognized")



def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "You : " + query)
    msgs.insert(END, "Friday : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)





frame = Frame(main)
sc=Scrollbar(frame)
sc1=Scrollbar(frame, orient='horizontal')
msgs=Listbox(frame, bg='white', fg='midnight blue', width=80, height=20 , xscrollcommand=sc1.set, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)
sc1.pack(side=BOTTOM, fill=X)
sc1.config(command=msgs.xview)
msgs.pack(side=LEFT, fill=BOTH, pady=10, padx=5)
frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10, padx=4)

btn = Button(main, text="Ask from F.R.I.D.A.Y.", bg='white', fg='DarkOrchid3', font=("Verdana", 16), command=ask_from_bot)
btn.pack()


def enter_function(event):
    btn.invoke()



main.bind('<Return>',enter_function)

def repeatL():
    while True:
        takeQuery()

t = threading.Thread(target=repeatL)

t.start()
 
main.mainloop()
