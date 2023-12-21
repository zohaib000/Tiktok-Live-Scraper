from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import csv
import os
import requests
from selenium.webdriver.support.ui import Select
import openpyxl
from datetime import datetime
import os
from selenium.webdriver.support.ui import Select
import csv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import openpyxl
from .sheet import write_new_row


def get_driver():
    options = Options()
    # options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
    path=os.path.join(os.getcwd(),"chrome_profile")
    options.add_argument(f"--user-data-dir={path}")
    options.add_argument(f"--headless")
    options.add_argument(f"--log-level=3")
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    # time.sleep(5000)
    action = ActionChains(driver)
    
    return driver,action


def get_comments(stream_url):
    # driver.switch_to.new_window(stream_url)
    # driver.get(stream_url)
    driver,action=get_driver()
    try:
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,'//div[@data-e2e="chat-message"]')))
    except:
        pass
    html=driver.find_element(By.XPATH,"//html").get_attribute('outerHTML')
    soup=BeautifulSoup(html,"html.parser")
    with open("soup.html",'w',encoding="utf-8") as f:
        f.write(soup.prettify())
    chats = soup.find_all('div', {'data-e2e': 'chat-message'})
    chats = chats[-20:]
    chats_data=[]
    for chat in chats:
        username=chat.find("span",attrs={"data-e2e":"message-owner-name"})
        username=str(username.text).strip() if username else "NoUser"
        message=chat.find("span",class_="tiktok-1kue6t3-DivComment e11g2s304")
        message=str(message.text).strip() if message else "NoMessage"
        chats_data.append({"username":username,"message":message})
    return chats_data




def scrapeStream(stream,keyword):
    channel_name=stream.find('p',attrs={"data-e2e":"search-card-user-unique-id"})
    channel_name=channel_name.text if channel_name else "NoUser"
    channel_url=f"https://www.tiktok.com/@{channel_name}"
    # scraping additional data from channel url
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0"
    }

    soup = BeautifulSoup(requests.get(channel_url, headers=headers).content, "html.parser")
    data=str(soup.prettify())
    current_date = datetime.now().strftime("%d %b, %Y")
    follower_count = re.search(r'"followerCount":(\d+)', data).group(1)
    following_count = re.search(r'"followingCount":(\d+)', data).group(1)
    likes_count = re.search(r'"heart":(\d+)', data).group(1)
    # bio scrapping
    Bio=None
    signature_match = re.search(r'"signature":"([^"]+)"', data)
    if signature_match:
        Bio = signature_match.group(1)
    else:
        Bio="No Bio."

    # finding stream details like viewers & last 20 chats !
    viewers=stream.find_all('div',class_="css-3b5hbd-LiveText ej426ge2")[1]
    viewers=viewers.text if viewers else "Not Found"

    # finding lst 20 chats of stream
    stream_url=f"https://www.tiktok.com/@{channel_name}/live"
    chats=[]

    # sending data to google sheet
    data={
        "channel_name":channel_name,
        "channel_url":channel_url,
        "followers_count":follower_count,
        "following_count":following_count,
        "likes_count":likes_count,
        "bio":Bio,
        "stream_url":stream_url,
        "concurrent_viewers":viewers,
        "current_date":current_date,
        "keyword":keyword,
    }
    values_list = list(data.values())
    write_new_row(values_list)

    # printing data
    print(data)
    print("-------------------------------------------------------------------------\n")



def searchLive(keyword):
    driver,action=get_driver()
    # for i in range(10):
    #     from .views import is_scraping
    #     if is_scraping:
    #         time.sleep(1)
    #         print(f"{keyword}-scraping")
    #     else:
    #         print(f"{keyword}-scraping stopped!")
    #         return 

    driver.get(f"https://www.tiktok.com/search/live?q={keyword}")
    StreamSet=list(set())

    while True:
        from .views import is_scraping
        if is_scraping:
            WebDriverWait(driver,20).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"css-1soki6-DivItemContainerForSearch.e19c29qe10")))
            soup=BeautifulSoup(driver.page_source,"html.parser")
            liveStreams=soup.find_all('div',class_="css-1soki6-DivItemContainerForSearch e19c29qe10")
            for s in liveStreams:
                unique_id=s.find('p',attrs={"data-e2e":"search-card-user-unique-id"})
                if unique_id not in StreamSet:
                    scrapeStream(s,keyword)
                    StreamSet.append(unique_id)

            # checking if no more results
            try:
                driver.find_element(By.XPATH,'//div[contains(text(),"No more results")]')
                print("All results scraped")
                break
            except:
                action.send_keys(Keys.CONTROL,Keys.END).perform()
                time.sleep(1)
        else:
            print(f"{keyword}-scraping stopped!")
            return 
            

    print(len(StreamSet))




# searchLive("sports")
# get_comments("https://www.tiktok.com/@emxxrr/live")
