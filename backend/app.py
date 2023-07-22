import requests

url = input("url: ")

def fetch_data(url):
    data = requests.get(url)
    return data.text

