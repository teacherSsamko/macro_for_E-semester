import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="/Users/ssamko/Documents/pythonStudying/selenium/chromedriver")
url = 'https://cls4.edunet.net/cyber/cm/mcom/pmco000b00.do'
driver.get(url)

with open("tickle.json") as f:
    secrets = json.loads(f.read())

def get_secret(key, secrets=secrets):
    try:
        return secrets[key]
    except:
        return "No secret like that"



# Login
driver.find_elements_by_css_selector('.btn_login.open_button')[1].click()
driver.find_element_by_css_selector('.dd_1').click()
driver.find_element_by_id('login_id').send_keys('ssamko')
driver.find_element_by_id('password').send_keys(get_secret("password"))
driver.find_element_by_id('password').send_keys(Keys.ENTER)

# Enter my class
# javascript:enterClass(224199)
# driver.find_elements_by_css_selector('.main_class_list li .btn_entrance')[0].click()

# wait til loaded

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'.btn_entrance'))
    )

finally:
    driver.find_elements_by_css_selector('.btn_entrance')[2].click()

# roll check
driver.find_elements_by_xpath("//ul[@class='cm_list']/li[@class='tit']")[0].click()

# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR,'.cm_list'))
#     )

# finally:
#     driver.find_elements_by_xpath(".//.cm_list/.tit").click()


# https://cls4.edunet.net/cyber/pm/prsa/pprs000a00.do 학급방