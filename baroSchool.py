import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import class_list

driver = webdriver.Chrome(
    executable_path="/Users/ssamko/Documents/pythonStudying/selenium/chromedriver")
url = 'https://tea.xn--9d0bm3su1cmz8a.com/'
driver.get(url)

with open("tickle.json") as f:
    secrets = json.loads(f.read())


def get_secret(key, secrets=secrets):
    try:
        return secrets[key]
    except:
        return "No secret like that"


# Login
driver.find_elements_by_css_selector('input.input')[0].send_keys('s110000577')
driver.find_elements_by_css_selector('input.input')[1].send_keys('19460401')
driver.find_element_by_css_selector('button.is-success').click()

# wait til page loaded
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.notification'))
    )

finally:
    select = driver.find_elements_by_css_selector('input.input')[0]

# Put school info
# 'input.input' 0 > school, 1 > grade, 2 > class
# access to school value
# select = driver.find_elements_by_css_selector('input.input')[0]

# driver.execute_script("arguments[0].value = '각리초등학교';", select)


driver.find_elements_by_css_selector('input.input')[1].send_keys('4')


driver.find_elements_by_css_selector(
    'input.input')[2].send_keys('5')
# students list
driver.find_elements_by_css_selector(
    'textarea')[0].send_keys("이은섭, 김은섭, 박은섭, 정은섭, 최은섭")

# search
driver.find_elements_by_css_selector('button.is-info')[1].click()

# wait til search finished
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button.is-success.is-fullwidth'))
    )

finally:
    driver.find_elements_by_css_selector(
        'button.is-success.is-fullwidth')[0].click()
