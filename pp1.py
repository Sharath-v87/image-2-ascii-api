import requests

path=input("enter the path of your image : ")
baseurL='https://image2ascii.herokuapp.com/uploadfile/'
f = open(path, 'rb')
files = {"file": (f.name, f, "multipart/form-data")}
x=requests.post(url=baseurL, files=files)
a=x.json().get('op')
print(a)
#print(type(contents))
#requests.post(url=baseurL,files=contents)