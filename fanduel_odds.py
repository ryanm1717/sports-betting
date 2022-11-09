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

#changing chromedriver default options
options = Options()
options.add_experimental_option("detach", True)
#options.headless = True
#options.add_argument('window-size=1920x1080') #Headless = True

web = 'https://www.fanduel.com/'
#path = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(web)
driver.maximize_window()
