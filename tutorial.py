from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/ssamko/Documents/pythonStudying/selenium/chromedriver")
url = 'https://cls4.edunet.net/cyber/cm/mcom/pmco000b00.do'
driver.get(url)

driver.find_elements_by_css_selector('a.btn_login')[1].click()
driver.find_elements_by_css_selector('dd.dd_2')[0].click()
driver.find_element_by_id('login_id').send_keys('c1282979')
driver.find_element_by_id('password').send_keys('c1282979!')
driver.find_element_by_id('password').send_keys(Keys.ENTER)

