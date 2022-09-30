#!/usr/local/bin/python3.8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
from bs4 import BeautifulSoup
import credential
from selenium.webdriver.firefox.options import Options as FirefoxOptions

mail = credential.mail
pw = credential.pw

## firefox_options = Options()
## firefox_options.add_argument("--headless")
## driver = webdriver.Firefox(options=firefox_options)

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("https://www.polito.it/")

# login
print('Starting login')
mail_input = driver.find_element_by_id("email")
mail_input.send_keys(mail)
pw_input = driver.find_element_by_id("password")
pw_input.send_keys(pw)
button_login = driver.find_element_by_id("login-button")
button_login.click()

driver.get('https://didattica.polito.it/pls/portal30/sviluppo.pagina_studente_2016.main')

driver.close()
