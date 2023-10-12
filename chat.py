import json
import os
import webbrowser
from asyncio import sleep

import pyaudio
import pywhatkit
import speech_recognition as sr
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render


def chatbotlisten(request):      
 try:
    dataa = json.loads(request.body)
    action = dataa['action']
    lis=sr.Recognizer()
    with sr.Microphone()as source:
      print('listen')
      voice=lis.listen(source)
      command=lis.recognize_google(voice)
      command = command.lower()
      print(command)
      webbrowser.register('chrome',None,
      webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))
      if('samsung') in command:
        link='http://127.0.0.1:8000/search/?q=samsung'
        webbrowser.get('chrome').open_new(link)
      elif('sony') in command:
        link='http://127.0.0.1:8000/search/?q=sony'
        webbrowser.get('chrome').open_new(link) 
      elif('redmi') in command:
        link='http://127.0.0.1:8000/search/?q=redmi'
        webbrowser.get('chrome').open_new(link) 
      elif('lenovo') in command:
        link='http://127.0.0.1:8000/search/?q=lenovo'
        webbrowser.get('chrome').open_new(link)
      else:
        link= 'http://127.0.0.1:8000/notfound/'
        webbrowser.get('chrome').open(link)
                
      print('Action:', action)        
      chatbotlisten(request)
      return render(request,'parts/chatbot.html',{})     
 # os.system('Notepad')    
 except json.decoder.JSONDecodeError:
      # 👇️ this runs
      print('The string does NOT contain valid JSON')
