# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 07:53:20 2024

@author: Dubai
"""

import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import webbrowser as wb
import time


engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def time_():
    t = datetime.datetime.now().strftime("%I:%M:%S")
    speak(" The current time is")
    engine.runAndWait()
    speak(t)
    
    
def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    
    speak(" The current date is")
    engine.runAndWait()
    speak(day)
    speak(month)
    speak(year)
        
    
def wish_me():
    speak("welcome back")
    
    # greatings 
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning, Omar")
        
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, Omar")
        
    elif hour >= 18 and hour < 24:
        speak("Good Evening, Omar")
        
    else:
        speak("Good Night, Omar")
        
    speak("My friend, please tell me how can i help you? ")
    

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ..... ")
        r.pause_threshold = 1.1
        audio = r.listen(source)
        
    try:
        print("Recognizing ..... ")
        query = r.recognize_google(audio, language='en-US')
        print(query)
        
    except Exception as e:
        print(e)
        print(" Say that again please ....")
        return None
    
    return query


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login('Your_Email', 'Your_Password')
    server.sendmail('Your_Email', to, content)
    server.close()
    
        


if __name__ == "__main__":
    
    wish_me()
        
    while True:
        query = take_command().lower()
    
        if "time" in query:
            time_()
            
        elif "date" in query:
            date_()
            
            
        elif 'send email' in query:
            try:
                speak("What should I write in subject ?")
                subject = take_command().capitalize()
                
                speak("What should I write in message ?")
                message = take_command()
                
                content = f"Subject: {subject} \n\n {message}"
                
                speak("Who is the Reciever?")
                reciept = input("Enter recieptant's name: ")
                
                to = (reciept)
                send_email(to,content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")
                
        elif 'search in chrome' in query:
            speak(" what should I search ? ")
            chromepath = "C:/Users/Dubai/AppData/Local/Google/Chrome/Application/chrome.exe  %s"
            search = take_command().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
            
            
        elif 'open youtub' in query:
            speak(" what should I search ? ")
            search_term = take_command().lower()
            wb.open('https://www.youtube.com/results?search_query='+search_term)
            time.sleep(5)
                
        elif 'search in google' in query:
            speak(" what should I search ? ")
            search_term = take_command().lower()
            speak(" Searching ....")
            wb.open('https://www.google.com/search?q'+search_term)
                
        
        elif 'stop listen' in query:
            speak(' For how many second you want me to stop listening to your commands ? ')
            ans = int(input("Enter the number of seconds : "))
            time.sleep(ans)
            print(ans)
            
            
            
                
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    