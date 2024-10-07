from solvers.svgcaptcha import solver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
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

#------Go to capcha_frame---------------------

WebDriverWait(driver, 5).until(
     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#__next > section > main > section > div > div > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active.home-search > div.ant-row.styles__SearchFormWrapper-sc-cmt9o6-6.dCdxPv > div.ant-col.ant-col-8 > form > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > div > div.ant-col.ant-form-item-control-wrapper > div > span > div > img"))
)

capcha_frame = driver.find_element(By.CSS_SELECTOR, "#__next > section > main > section > div > div > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active.home-search > div.ant-row.styles__SearchFormWrapper-sc-cmt9o6-6.dCdxPv > div.ant-col.ant-col-8 > form > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > div > div.ant-col.ant-form-item-control-wrapper > div > span > div > img")
src_value = capcha_frame.get_attribute("src")

encoded = src_value.replace("data:image/svg+xml;base64,", "")
decoded = base64.b64decode(encoded)
captcha = solver.solve_captcha(decoded)

print(captcha)
time.sleep(100)
driver.quit()

