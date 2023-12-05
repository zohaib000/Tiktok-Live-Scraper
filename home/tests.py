import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import concurrent.futures
import json
from fake_useragent import UserAgent
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import concurrent.futures

def openProfile(i):
    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir=C:\\Users\Administrator\\Desktop\\youtube views bot\\Chrome Profiles\\profile-{i-1}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    driver.get("https://youtube.com")
    time.sleep(10000)

openProfile(23)
