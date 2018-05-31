from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import os

import time

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/aakashravi/selrandom/speech-recognition.json"
os.environ['webdriver.chrome.driver']='/usr/bin/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("--no-sandbox")




# Google Chrome
driver = webdriver.Chrome(chrome_options=options)
# ------------------------------
# The actual test scenario: Test the codepad.org code execution service.

# Go to codepad.org
driver.get('http://chat.gubagoo.com/')

time.sleep(6)

driver.find_element_by_id('account_id').send_keys('100268')

driver.find_element_by_id('username').send_keys('Abhijitks')

driver.find_element_by_id('password').send_keys('Roberthyden007')

driver.find_element_by_id('submit').click()

#driver.find_element_by_xpath('//*[@id="mini_popup_wrapper"]/input[2]').click()

driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/ul/li[3]/a').click()

time.sleep(3)
driver.find_element_by_xpath('//*[@id="historyFilterForm"]/div[11]/input[1]').click()



# name of my select filter_account_id


time.sleep(3)
driver.find_element_by_xpath('//*[@id="from"]').send_keys("sending")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="from"]').clear()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="from"]').send_keys("2018-03-01")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="from"]').send_keys(Keys.RETURN)

driver.find_element_by_xpath('//*[@id="to"]').send_keys("sending")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="to"]').clear()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="to"]').send_keys("2018-03-01")

driver.find_element_by_xpath('//*[@id="to"]').send_keys(Keys.RETURN)



import time

time.sleep(1)

driver.find_element_by_xpath('//*[@id="historyFilterForm"]/div[11]/input[1]').click()



def callperday(driver):



    count=0

    for i in range(100,1000):

     print(count)
     print(i)
     #time.sleep(3)
     driver.get('https://gb1.gubagoo.com/chat/history/index/page/' + str(i))

     time.sleep(1)

     table = driver.find_element_by_xpath('//*[@id="historyTable"]/table/tbody')
     atags = table.find_elements(By.TAG_NAME, 'a')

     for each in atags:
        if (each.get_attribute('class') == 'view-link colorbox cboxElement'):
            print(each.get_attribute('href'))
            count=count+1
            fd = open('hrefs1.csv', 'a')

            fd.write(each.get_attribute('href') + "\n")
            fd.close()


time.sleep(5)
callperday(driver)
