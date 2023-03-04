from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import requests

def get_video_id(link, id):
    

    cookies = {
        '_ga': 'GA1.2.1922949325.1677776852',
        '_gid': 'GA1.2.2014378703.1677776852',
        '__gads': 'ID=f4cda8988d895a57-223f30f029dc0031:T=1677776853:RT=1677776853:S=ALNI_MZ3tLPUJ7FgeEyfTkZOclsQkY8QWQ',
        '__gpi': 'UID=00000be052f713af:T=1677776853:RT=1677776853:S=ALNI_MbvRQYg4RcYOg5bgCMetpAbh-8N7g',
        '_gat_UA-3524196-6': '1',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_ga=GA1.2.1922949325.1677776852; _gid=GA1.2.2014378703.1677776852; __gads=ID=f4cda8988d895a57-223f30f029dc0031:T=1677776853:RT=1677776853:S=ALNI_MZ3tLPUJ7FgeEyfTkZOclsQkY8QWQ; __gpi=UID=00000be052f713af:T=1677776853:RT=1677776853:S=ALNI_MbvRQYg4RcYOg5bgCMetpAbh-8N7g; _gat_UA-3524196-6=1',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not A(Brand";v="24", "Chromium";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'MlNhdDQ1',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)

    downloadSoup = BeautifulSoup(response.text, 'html.parser')


    downloadURL = downloadSoup.a["href"]

    mp4_file = urlopen(downloadURL)

    with open(f"downloads/{id}.mp4", "wb") as f:
        while True:
            data = mp4_file.read(4096)
            if data:
                f.write(data)
            else:
                break

driver = webdriver.Chrome()
driver.get("Link to your TikTok Account Page")  

time.sleep(1)

scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
i = 1

while True:
    # scroll one screen height each time
    driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
    i += 1
    time.sleep(scroll_pause_time)
    # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
    scroll_height = driver.execute_script("return document.body.scrollHeight;")  
    # Break the loop when the height we need to scroll to is larger than the total scroll height
    if (screen_height) * i > scroll_height:
        break

soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup.prettify())
liked_videos = soup.find_all('div', class_='tiktok-yz6ijl-DivWrapper')
print(len(liked_videos))

for index, video in enumerate(liked_videos):
    get_video_id(video.a['href'], index)
    time.sleep(10)

