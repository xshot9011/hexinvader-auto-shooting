import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(os.path.join('chromedriver', 'chromedriver'+str(sys.argv[1]))+'.exe')
driver.get('http://www.hexinvaders.com/')

while True:
    current_code = driver.find_element_by_id("current-color").text

    invader_elements = driver.find_elements_by_class_name("invaderLabel")
    spaces = driver.find_elements_by_class_name("space")

    try:
        invader_codes = [ele.get_attribute('textContent') for ele in  invader_elements]
        spaces[invader_codes.index(current_code)].click()
    except :
        pass
    time.sleep(0.2)
driver.quit()
