"""This python script reads a json file from an url and properly parse the Json data, it then look for the key 
"thumbnail" to find the url of a thumbnail to be download to local storage"""
import urllib.request
import json

req = urllib.request.Request("https://raw.githubusercontent.com/g0v/g0v.tw/master/g0v.json")
file = urllib.request.urlopen(req)
jsonData = json.loads(file.read())

thumbnail = jsonData ["thumbnail"]
print(thumbnail)

urllib.request.urlretrieve(thumbnail, "thumbnail.png")
