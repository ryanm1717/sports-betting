# import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = 'C:\Program Files (x86)/chromedriver'
s = Service(path)
driver = webdriver.Chrome(service=s)

web = 'https://sportsbook.fanduel.com/navigation/nfl'
driver.get(web)
driver.maximize_window()

options = Options()
options.headless = True

#nfl = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div/div/div/a[6]')
#nfl.click()

#game_1 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div[3]/div/div[1]/a/div[1]/div/div/div/div[2]/span')
#print(game_1.text)

all_teams = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/div/div[3]/div')
print(all_teams)

#<div class="af ag ah ai cy cz aj s h i j ak l m al o am q an"><span class="ae aj je jf jg jh ia ib ic is ji s fm el jj h i j ak l m al o am q an bu">TEN Titans</span></div>