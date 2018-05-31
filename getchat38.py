#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
import time
import os
import urllib

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/aakashravi/PycharmProjects/callcenterautomation/speech-recognition.json"
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

driver.find_element_by_id('account_id').send_keys('100268')


driver.find_element_by_id('username').send_keys('Abhijitks')

driver.find_element_by_id('password').send_keys('Roberthyden007')

driver.find_element_by_id('submit').click()


driver.find_element_by_xpath('//*[@id="mini_popup_wrapper"]/input[2]').click()

import csv

with open('hrefsapril35.csv', encoding="utf-8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
      try:
           driver.get(row[0])
           print("url"+row[0])
           time.sleep(1)
           chat_id = driver.find_element_by_class_name('form-element').text
           chat_id = chat_id.replace("#", "")
           chat_id = chat_id.replace("\n", '')
           chat_id = chat_id.replace(":", "-")
           fd = open(chat_id +'.csv', 'a', encoding="utf-8")

           fd.write(driver.find_element_by_id('messenger').text.replace(",",""))

           print(driver.find_element_by_id('messenger').text)

           listvalues = driver.find_elements_by_class_name('value')

           fd.write("\n------------------------------------------\n")
           for each in listvalues:
               print(each.text)
               fd.write(each.text + "\n")

           fd.close()
           import urllib.request

           # get the image source
           gg=driver.find_elements(By.CLASS_NAME,'gg-image')
           if(len(gg)>0):
             img = gg[0].find_elements(By.TAG_NAME,'img')

             if(len(img)>0):
                 src = img[0].get_attribute('src')
                 urllib.request.urlretrieve(src, chat_id + ".png")
                 from google.cloud import storage

                 client = storage.Client()
                 bucket = client.get_bucket('callcenterchatapril')

                 blob = bucket.blob(chat_id+"/"+chat_id + ".png")
                 blob.upload_from_filename(chat_id + ".png")
                 print("uploaded")
                 os.remove(chat_id + ".png")




           from google.cloud import storage

           client = storage.Client()
           bucket = client.get_bucket('callcenterchatapril')

           blob = bucket.blob(chat_id+"/"+chat_id + '.csv')
           blob.upload_from_filename(chat_id + '.csv')
           print("uploaded")
           os.remove(chat_id + '.csv')
      except Exception as e:
          print(e)
