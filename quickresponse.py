from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/aakashravi/PycharmProjects/callcenterautomation/speech-recognition.json"


from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# maximized window
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--kiosk");

# Google Chrome
driver = webdriver.Chrome('/Users/aakashravi/PycharmProjects/callcenterautomation/chromedriver3')

# ------------------------------
# The actual test scenario: Test the codepad.org code execution service.

# Go to codepad.org
driver.get('http://chat.gubagoo.com/')

driver.find_element_by_id('account_id').send_keys('100268')


driver.find_element_by_id('username').send_keys('Abhijitks')

driver.find_element_by_id('password').send_keys('Roberthyden007')

driver.find_element_by_id('submit').click()


driver.find_element_by_xpath('//*[@id="mini_popup_wrapper"]/input[2]').click()

time.sleep(3)

driver.get('https://gb1.gubagoo.com/chat/settings/quick-responses')

driver.find_element_by_xpath('//*[@id="mini_popup_wrapper"]/input[2]').click()

time.sleep(3)

import csv

with open('user6.csv',encoding="utf-8") as csvfile:

        readCSV = csv.reader(csvfile, delimiter=',')

        for row in readCSV:
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="inline-account-picker"]/div[1]/form/input').clear()
            time.sleep(1)
            driver.find_element(By.XPATH,'//*[@id="inline-account-picker"]/div[1]/form/input').send_keys(row[1])
            time.sleep(1)



            driver.find_element(By.XPATH,'//*[@id="inline-account-picker"]/div[1]/form/button[1]').click()

            time.sleep(1)


            ul=driver.find_elements_by_xpath('//*[@id="data_responses"]/ul')
            #//*[@id="data_responses"]/ul
            if(len(ul)>0):
              inputs=ul[0].find_elements(By.TAG_NAME,'input')
              for each in inputs:
                 print(each.get_attribute('value'))
                 fd = open(row[0]+'.csv', 'a',encoding="utf-8")
                 fd.write(each.get_attribute('value'))
                 fd.write('\n\n\n')
                 fd.close()



            elements=driver.find_elements(By.TAG_NAME,'textarea')
            for each in elements:
                print(each.get_attribute('value'))
                fd = open(row[0]+'.csv', 'a',encoding="utf-8")
                fd.write(each.get_attribute('value'))
                fd.write('\n\n\n')
                fd.close()
            if(len(elements)>0):
               from google.cloud import storage

               client = storage.Client()
               bucket = client.get_bucket('callcenterquickresponse')

               blob = bucket.blob(row[0]+'.csv')
               blob.upload_from_filename(row[0]+'.csv')
               print("uploaded" + row[0]+'.csv')
               os.remove(row[0]+'.csv')


time.sleep()




driver.close()

