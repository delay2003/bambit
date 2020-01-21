#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests as req
import os

print(os.system('arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 test2.wav' ))
cmd1 = "scp 'test2.wav' ubuntu@13.124.243.109:~/bigdataAnalytics/restFileUpload"
print(os.system(cmd1))
filename=os.getcwd()+'/'+'files/a.txt'
files = {'myfile': open(filename,'rb')}
url="http://13.124.243.109:8080/upload"
response = req.post(url, files=files )
