from picamera import PiCamera
from time import sleep
from requests import get
import json
from pprint import pprint

camera = PiCamera()

camera.start_preview()
camera.annotate_text = "11234190 11299982"
sleep(5)
camera.capture('/home/sel/Desktop/text.jpg')
camera.start_recording('/home/sel/Desktop/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583'
weather = get(url).json()['items']
pprint(weather)
