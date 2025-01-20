from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service('chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get(url)

barra_buscadora = driver.find_element(By.NAME,'q')
barra_buscadora.send_keys('Celulares')
barra_buscadora.send_keys(Keys.ENTER)