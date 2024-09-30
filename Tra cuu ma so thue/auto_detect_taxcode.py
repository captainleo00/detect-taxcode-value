from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key,  Controller
import os
import time
from get_taxcode_data import data
import requests
import base64


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#-------------Go to taxcode_web---------------------

driver.get("https://hoadondientu.gdt.gov.vn/")

#------Hide_intro---------------------
WebDriverWait(driver, 5).until(
     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "body > div:nth-child(4) > div > div.ant-modal-wrap > div > div.ant-modal-content > button > span > i > svg"))
)

hidden_button1 = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(4) > div > div.ant-modal-wrap > div > div.ant-modal-content > button > span > i > svg")
hidden_button1.click()

#------Go to taxcdoe_detect_tag---------------------

WebDriverWait(driver, 5).until(
     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#__next > section > main > section > div > div > div > div > div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child(1) > div:nth-child(2)"))
)

taxcode_detect_tag = driver.find_element(By.CSS_SELECTOR, "#__next > section > main > section > div > div > div > div > div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child(1) > div:nth-child(2)")
taxcode_detect_tag.click()

#------Input-taxcode---------------------

WebDriverWait(driver, 5).until(
     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#mst"))
)

input_taxcode_field = driver.find_element(By.CSS_SELECTOR, "#mst")
input_taxcode_field.click()
input_taxcode_field.send_keys(data)

time.sleep(600)    
driver.quit()