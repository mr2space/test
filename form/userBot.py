import base64
from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Constants import *
import os

os.environ['PATH'] += r""


options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:8080")
service = Service(r"C:\Users\princ\OneDrive\Desktop\new project\selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service,options=options)

driver.get('https://forms.gle/WT68aV5UnPajeoSc8')

driver.implicitly_wait(10)

input = driver.find_element(By.XPATH, full_nameXpath)
input.send_keys("Prince Goswami")
input = driver.find_element(By.XPATH, phone_numberXpath)
input.send_keys("7393085743")
input = driver.find_element(By.XPATH, emailXpath)
input.send_keys("princegoswami.work@gmail.com")
input = driver.find_element(By.XPATH, addressXpath)
input.send_keys("Ed-2/12 ADA colony Naini Prayagraj")
input = driver.find_element(By.XPATH, pincodeXpath)
input.send_keys("211008")
input = driver.find_element(By.XPATH, dob_Xpath)
input.send_keys("24122004")
input = driver.find_element(By.XPATH, genderXpath)
input.send_keys("male")
input = driver.find_element(By.XPATH, code_Xpath)
input.send_keys("GNFPYC")
input = driver.find_element(By.XPATH, submit_Xpath)
input.click()
print("form Submitted")




