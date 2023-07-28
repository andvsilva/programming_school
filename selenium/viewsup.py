import os
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

locations=['US',
           'CA',
           'DE',
           'NL',
           'NO',
           'RO',
           'CH',
           'TR'
           ]

npapers  = [1]
titlepapers = {1 : "",
              }

while True:
    location = random.choice(locations)

    print(f" >>> Connecting to {location}")
    os.system(f"windscribe connect {location}")

    time.sleep(4)
    
    ipaper = int(random.choice(npapers))
    titlepaper = titlepapers[ipaper]

    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    driver.get(f"{titlepaper}")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav"]/li[6]/a'))).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/section[2]/div/div/div/div[2]/h3/a"))).click()
    
    height = driver.execute_script("return document.body.scrollHeight")
    
    for scrol in range(100,height,100):
        delay = random.randint(1,4)
        driver.execute_script(f"window.scrollTo(0,{scrol})")

        time.sleep(delay)
        
    ntime = random.randint(120,300)
    print(f"sleeping for {ntime}s...")
    time.sleep(ntime)
    os.system("pkill chrome")

    ntime = random.randint(60,120)
    print(f"sleeping for {ntime}s...")
    time.sleep(ntime)