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

narticles  = [1, 2, 3, 4, 5, 7, 8, 9]

titlearticles = {1 : "https://andrevsilva.com",
               2 : "https://andrevsilva.com/1paper.html",
               3 : "https://andrevsilva.com/2paper.html",
               4 : "https://andrevsilva.com/3paper.html",
               5 : "https://andrevsilva.com/4paper.html",
               6 : "https://andrevsilva.com/5paper.html",
               7 : "https://andrevsilva.com/6paper.html",
               8 : "https://andrevsilva.com/7paper.html",
               9 : "https://andrevsilva.com/8paper.html"
          }


def scroldownpage(driver):
    height = driver.execute_script("return document.body.scrollHeight")
    
    for scrol in range(100,height,500):
        delay = random.randint(1,4)
        driver.execute_script(f"window.scrollTo(0,{scrol})")

        time.sleep(delay)

def newtab(titlearticle, driver):
    driver.switch_to.new_window('tab')
    driver.implicitly_wait(1)
    driver.get(titlearticle)

def get_title(iarticle):
    titlearticle = titlearticles[iarticle]
    return titlearticle

def long_sleep():
    ntime = random.randint(60,90)
    print(f"long sleep for {ntime}s...")
    time.sleep(ntime)

def short_sleep():
    ntime = random.randint(20,35)
    print(f"short sleep for {ntime}s...")

def access_articles():

    titlearticle = titlearticles[1] # homepage
    
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    driver.get(f"{titlearticle}")

    for iarticle in range(2,len(narticles)+1):
        titlearticle = get_title(iarticle)
        newtab(titlearticle, driver)
        scroldownpage(driver)
        delaytime = random.randint(1,5)
        time.sleep(delaytime)


while True:
    location = random.choice(locations)

    print(f" >>> Connecting to {location}")
    os.system(f"windscribe connect {location}")

    delaytime = random.randint(1,7)
    time.sleep(delaytime)

    access_articles()
    
    long_sleep()
    os.system("pkill chrome")

    short_sleep()
    
    

