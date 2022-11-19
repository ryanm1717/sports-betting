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

options = Options()
options.headless = True

path = 'C:\Program Files (x86)/chromedriver'
s = Service(path)
driver = webdriver.Chrome(service=s, options=options)

web = 'https://sportsbook.fanduel.com/navigation/nfl'
driver.get(web)
driver.maximize_window()



# use full xpath
all_teams = driver.find_elements(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/div/div/div[1]/div/div[3]/div')
print(all_teams[0].text)



driver.quit()