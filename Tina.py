#!/usr/bin/env python2.7\
# ========================================================================================================================
# Author      : Mr.R.Meena                              
# Created By  : Naveen Balasundar
# Date Created: 02-03-2018
# Date last Modified: 011-08-2018
#
# ========================================================================================================================
# Imports
# ========================================================================================================================
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,Trainer
import os
#from espeak import espeak
import wikipedia
import wolframalpha
import cv2,time
import os
import datetime
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
#
#==================================================================================================================================
localtime = time.asctime(time.localtime(time.time()))
print("Tina: WELCOME. I'm Tina,your virtual assistant")
speak.Speak("WELCOME. I'm Tina,your virtual assistant")

while True:
   
    input=raw_input("you: ")
    if input!="wiki":

        if  input=="open camera":
                speak.Speak("opening camera ")
                video=cv2.VideoCapture(0)
                a=0
                while (True):
                    a=a+1

                    check,frame=video.read()

                    print(check)
                    print(frame)

                    cv2.imshow("capture                press x to exit",frame)


                    key=cv2.waitKey(1)
                    if key==ord("x"):
                        break
                #print(a)

                video.release()
                cv2.destroyAllWindows
        
        
        elif input=="who are you":
                print ("I am Tina")
                speak.Speak("I am Tina")
                    
        elif input=="tell about you" :
                print("I am Tina,a virtual but still in developing assistant I was created by Naveen")
                speak.Speak("I am Tina,a virtual but still in developing assistant I was created by Naveen")

        else:
              
                bot = ChatBot('Bot')
                bot.set_trainer(ListTrainer)
                """change the below directory and in comment to train your module.
                after that comment those three line amd run the program"""
                #for Files in os.listdir('C:/Users/USER\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\TempState\Downloads\chatterbot-corpus-master\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
                  # data = open('C:/Users/USER\AppData\Local\Packages\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\TempState\Downloads\chatterbot-corpus-master\chatterbot-corpus-master\chatterbot_corpus\data\english/'+Files,'r').readlines()
                   #bot.train(data)
                         
                if input.strip() !="bye":
                   reply=str(bot.get_response(input))
                   print("Tina: "+reply)
                   speak.Speak(reply)
                if input=="bye":
                  print("bye")
                  speak.Speak("bye, see you later")
                  break 
    if(input=="wiki"):
         input=raw_input("you: ")

         try:
            #get your own wolframalpha api id and paste below#
            app_id = "2H365T-KAEX9G8XA3"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print (res)
            speak.Speak(res)
    
         except:
        
            wiki= wikipedia.summary(input)
            print (wiki)
            speak.Speak(wiki)
            


                
