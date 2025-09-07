import requests
url = "http://flask_app:5000/add"
data = {"title" : "test"}

requests = requests.post(url, data=data)
print(requests)