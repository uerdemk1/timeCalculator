import json
import requests
import os

headers = {
    "Content-Type":"application/json"
}

url_timeZoneUTC = 'https://timeapi.io/api/Time/current/zone?timeZone=UTC'

s = requests.request('GET', url_timeZoneUTC, headers=headers, timeout=10)
#print("Code:", s.status_code)
if s.status_code == 200:
    isoTime = s.json()
    print("Time in ISO format: ", isoTime["dateTime"])
else:
    print("problem...(except)")

       