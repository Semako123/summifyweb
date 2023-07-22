import requests, re
from bs4 import BeautifulSoup
from transformers import pipeline

url = input("url: ")

def fetch_data(url):
    data = requests.get(url)
    return data.text


def extract_data(html_data):
    res_obj = {}
    soup = BeautifulSoup(html_data, "html.parser")
    body_text = soup.body.get_text()
    pattern = r"\n{2,}"
    # Use the re.sub() function to replace the matched pattern with a single carriage return
    body = re.sub(pattern, "\n", body_text)
    title = soup.title.string
    res_obj["title"] = title
    res_obj["body"] = body
    return res_obj


html_data = fetch_data(url)
data = extract_data(html_data)
print(data)


def summarize(text):
    pass
