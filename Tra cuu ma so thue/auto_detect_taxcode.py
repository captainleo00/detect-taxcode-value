from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import base64
from solvers.svgcaptcha import solver





def check_text_appearance(xpath, text1):
     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

     #-------------Go to taxcode_web---------------------

     driver.get("https://hoadondientu.gdt.gov.vn/")

     # Find file taxcode_requests.log

     data_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'taxcode_requests.log')

     # Read file taxcode_requests.log

     taxcode_value = None
     with open(data_file_path, 'r', encoding="utf-8") as file:
          lines = file.readlines()  

     # Find lasted data in file

     for line in reversed(lines): 
          if 'New taxcode request received:' in line:
               taxcode_value = line.split('New taxcode request received: ')[1].split(',')[0]  # Tách giá trị
          break
          # return taxcode_value

     print (taxcode_value)

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
     # input_taxcode_field.click()
     input_taxcode_field.send_keys(taxcode_value)
     input_taxcode_field.send_keys(Keys.TAB)

     #------Go to capcha_frame---------------------

     WebDriverWait(driver, 5).until(
          EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#__next > section > main > section > div > div > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active.home-search > div.ant-row.styles__SearchFormWrapper-sc-cmt9o6-6.dCdxPv > div.ant-col.ant-col-8 > form > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > div > div.ant-col.ant-form-item-control-wrapper > div > span > div > img"))
     )

     capcha_frame = driver.find_element(By.CSS_SELECTOR, "#__next > section > main > section > div > div > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active.home-search > div.ant-row.styles__SearchFormWrapper-sc-cmt9o6-6.dCdxPv > div.ant-col.ant-col-8 > form > div:nth-child(1) > div:nth-child(2) > div > div:nth-child(1) > div > div.ant-col.ant-form-item-control-wrapper > div > span > div > img")

     #------Get capcha_code---------------------

     src_value = capcha_frame.get_attribute("src") # Lấy thông tin source image
     encoded = src_value.replace("data:image/svg+xml;base64,", "") # Loại bỏ phần tiền tố, chỉ chừa lại dữ liệu base64 trong biến src_value
     decoded = base64.b64decode(encoded) # Giaỉ mã dữ liệu base64
     captcha = solver.solve_captcha(decoded) # Gỉai mã thành mã captcha

     print(captcha)

     #-------Fill captcha_code------------------


     fill_captcha = WebDriverWait(driver, 10).until(
          EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/section/main/section/div/div/div/div/div[3]/div[2]/div[2]/div[1]/form/div[1]/div[2]/div/div[2]/div/div[2]/div/span/input"))
     )

     fill_captcha = driver.find_element(By.XPATH, "/html/body/div/section/main/section/div/div/div/div/div[3]/div[2]/div[2]/div[1]/form/div[1]/div[2]/div/div[2]/div/div[2]/div/span/input")
     fill_captcha.send_keys(captcha)

     find_button = WebDriverWait(driver, 10).until(
     EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > section > main > section > div > div > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active.home-search > div.ant-row.styles__SearchFormWrapper-sc-cmt9o6-6.dCdxPv > div.ant-col.ant-col-8 > form > div.ant-row-flex.ant-row-flex-center.home-search-button > div > button"))
     )

     find_button = driver.find_element(By.CSS_SELECTOR, "#__next > section > main > section > div > div > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active.home-search > div.ant-row.styles__SearchFormWrapper-sc-cmt9o6-6.dCdxPv > div.ant-col.ant-col-8 > form > div.ant-row-flex.ant-row-flex-center.home-search-button > div > button")
     find_button.click()

     xpath = "/html/body/div/section/main/section/div/div/div/div/div[3]/div[2]/div[2]/div[2]/section/p"
     text1 = "đã đăng ký"

     try:
         
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, xpath), text1)
)
        return "Đã đăng ký hóa đơn điện tử" 
     except Exception as e:
        return "Chưa đăng ký hóa đơn điện tử"
     finally:
       driver.quit()

if __name__ == '__main__':
    xpath = "/html/body/div/section/main/section/div/div/div/div/div[3]/div[2]/div[2]/div[2]/section/p"
    text1 = "đã đăng ký"
    result = check_text_appearance(xpath, text1)
    print(f'Trạng thái mã số thuế: {result}')