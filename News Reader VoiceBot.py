from win32com.client import Dispatch
import requests
import json
def speak(string):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(string)

speak(" Hello , I am News Reader Bot , will be providing u with today's latest news ")

url1 = ('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=06dc1e6f5f4b4fbbb4a9ff65ea239a2b')

#For Entering Personal-url for News
#speak("Enter your url here")
#url1 = input("ENTER YOUR URL\n")

data = requests.get(url=url1)
news_data = data.json()

print(news_data['articles'][0]['description'])

for i in range(20):
    print(i,news_data['articles'][i]['source']['name'])

speak("choose your news paper number here")
news_no = int(input("CHOOSE NEWS PAPER NUMBER\n"))

speak("So Today's news is")
print(news_data['articles'][news_no]['title'])
speak(news_data['articles'][news_no]['title'])

print(news_data['articles'][news_no]['content'])
speak(news_data['articles'][news_no]['content'])

print(news_data['articles'][news_no]['description'])
speak(news_data['articles'][news_no]['description'])

print("FOR MORE INFO VISIT NEWS-WEBSITE , CLICK HERE",news_data['articles'][news_no]['url'])
speak("Thankyou ,That's it for today's News , Exiting now ")


