import requests

path=input("enter the path of your image : ")
baseurL='http://127.0.0.1:8000/uploadfile/'
f = open(path, 'rb')
files = {"file": (f.name, f, "multipart/form-data")}
x=requests.post(url=baseurL, files=files)
a=x.json().get('op')
print(a)
#print(type(contents))
#requests.post(url=baseurL,files=contents)