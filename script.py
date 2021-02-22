from bs4 import BeautifulSoup
import requests
import tweepy
import re
import time
from datetime import datetime

def twitter():
    consumer_key =""
    consumer_secret =""
    access_token =""
    access_token_secret =""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 
    print("\n[STARTING]")
    count = -1
    l = ["","",""]
    while True:
        count += 1
        d = ["","",""]
        t = (datetime.now()).strftime("%H:%M")
        try:  
            r = requests.get('https://www.worldometers.info/coronavirus/')
            soup = BeautifulSoup(r.text, 'html.parser')
            mydivs = soup.findAll("div", {"class": "maincounter-number"})
            d[0] = (re.sub('<[^>]+>','',str(mydivs[0]))).strip()
            d[1] = (re.sub('<[^>]+>','',str(mydivs[1]))).strip()
            d[2] = (re.sub('<[^>]+>','',str(mydivs[2]))).strip()
            final = str("👥Cases: "+d[0]+" ͏͏ ͏͏ ͏͏ ͏͏ ͏͏ ͏͏ ͏͏ ͏͏\n💀Dead: "+d[1]+" ͏͏ ͏͏ ͏͏ ͏͏ ͏͏ ͏͏ ͏͏ ͏͏\n🤸‍♂️Recovered: "+d[2]+" ͏͏ ͏͏\n⏳Last Updated: "+t+" CST")      
            api.update_profile(description=final)
            print(".",end="")
            if l == ["","",""]:
                for i in range(3):
                    l[i] = d[i]
            if count%6==0 and count>0:
                for i in range(3):
                    l[i] = str( abs(int((d[i]).replace(',', '')) - int((l[i]).replace(',', ''))))   
                final = str("Globally within the past hour…\n👥Cases: "+l[0]+"\n💀Dead: "+l[1]+"\n🤸‍♂️Recovered: "+l[2]+"\n#corona #coronavirus #covid2019 #covid19 #news")
                api.update_status(status=final)
                for i in range(3):
                        l[i] = d[i]
        except:
            print("\n[ERROR] Time is "+t+"\n")
            count = -1
            l = ["","",""]
        time.sleep(60*10)

def main():
    twitter()

main()
