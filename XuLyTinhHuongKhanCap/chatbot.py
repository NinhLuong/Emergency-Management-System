import os
from subprocess import call
import playsound
import speech_recognition as sr
import time
import datetime
import requests
from gtts import gTTS
from modules.Hardware import *

language = 'vi'

def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)    
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        print(   )
        audio = r.listen(source, phrase_time_limit=8)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print("...")
            return 0

def get_text():
    while True:
        text = get_audio()
        if text:
            return text.lower()
    return 0

def call114():
    Call("0824451334")
    speak("đang gọi 114")

def call113():
    Call("0824451334")
    speak("đang gọi 113")

def call115():
    Call("0824451334")
    speak("đang gọi 115")

def callbql():
    Call("0824451334")
    speak("đang gọi ban quản lý") 
    
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))

def current_weather():
    call_url = 'https://api.openweathermap.org/data/2.5/weather?lat=10.850145464871641&lon=106.7716601973813&appid=d80948795e2ec6257f1f62303cf81808&lang=vi'
    response = requests.get(call_url)
    data = response.json()
    city_res = data["main"]
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = int(city_res["temp"]-273)
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}% """.format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        speak(content)
        time.sleep(20)
    else:
        speak("Không tìm thấy địa chỉ của bạn")

def assistant():
    while True:
        text = get_text()
        if "thời tiết"  in text:
            current_weather()
        elif "ngày" in text or "giờ" in text or "tháng"  in text or" phút" in text or "năm" in text: 
            get_time(text)  
        elif "cháy" or " cứu hoả" in text:
            call114()
        elif " gọi cảnh sát" or "cướp"  or " gọi công an"in text:
            call113()
        elif "cứu thương" or " cấp cứu" in text:
            call115()
        elif "ban quản lý" in text:
            callbql()