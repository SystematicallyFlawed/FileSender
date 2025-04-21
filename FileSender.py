##imports##
import requests

url = 'https://192.168.209.115:5000/upload'
file_path = input("Path to the sending file: ")

with open(file_path, 'rb') as f:
    files = {'file': (file_path, f)}
    response = requests.post(url, files=files)

print(response.text)