from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

options = Options()
options.add_argument('start-maximized')
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)

driver.get("https://tiktok.com")

time.sleep(5)

print(driver.title)