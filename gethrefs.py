from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import os

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/aakashravi/PycharmProjects/callcenterautomation/speech-recognition.json"

# Google Chrome
driver = webdriver.Chrome('/Users/aakashravi/PycharmProjects/callcenterautomation/chromedriver')

# ------------------------------
# The actual test scenario: Test the codepad.org code execution service.

# Go to codepad.org
driver.get('http://chat.gubagoo.com/')

driver.find_element_by_id('account_id').send_keys('100268')

driver.find_element_by_id('username').send_keys('Abhijitks')

driver.find_element_by_id('password').send_keys('Roberthyden007')

driver.find_element_by_id('submit').click()

driver.find_element_by_xpath('//*[@id="mini_popup_wrapper"]/input[2]').click()

driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/ul/li[3]/a').click()

# name of my select filter_account_id

import time

time.sleep(5)

select = Select(driver.find_element_by_id('filter_account_id'))


def callperday(driver, clicks):



    count=0
    for i in range(1400,1500):
     print(count)
     print(i)
     driver.get('https://gb1.gubagoo.com/chat/history/index/page/' + str(i) + '?from=2018-05-24&amp;to=2018-05-24&amp;manage_account_id=100268&amp;show_auto_rating=1')
     #time.sleep(1)

     #driver.find_element_by_xpath('//*[@id="mini_popup_wrapper"]/input[2]').click()
     #time.sleep(1)
     time.sleep(1)

     table = driver.find_element_by_xpath('//*[@id="historyTable"]/table/tbody');
     atags = table.find_elements(By.TAG_NAME, 'a')

     for each in atags:
        if (each.get_attribute('class') == 'view-link colorbox cboxElement'):
            print(each.get_attribute('href'))
            count=count+1
            fd = open('hrefs11.csv', 'a')

            fd.write(each.get_attribute('href') + "\n")
            fd.close()


callperday(driver,0)
