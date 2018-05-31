from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/aakashravi/PycharmProjects/callcenterautomation/speech-recognition.json"


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

#name of my select filter_account_id

import time
time.sleep(5)





select = Select(driver.find_element_by_id('filter_account_id'))





def callperday(driver,select,trcount,tdcount,flag,datestr):


            driver.find_element_by_xpath('//*[@id="from"]').send_keys("sending")
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="from"]').clear()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="from"]').send_keys(datestr)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="from"]').send_keys(Keys.RETURN)

            driver.find_element_by_xpath('//*[@id="to"]').send_keys("sending")
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="to"]').clear()
            time.sleep(1)

            driver.find_element_by_xpath('//*[@id="to"]').send_keys(datestr)

            driver.find_element_by_xpath('//*[@id="to"]').send_keys(Keys.RETURN)

            #//*[@id="historyFilterForm"]/div[11]/input[1]

            driver.find_element_by_xpath('//*[@id="historyFilterForm"]/div[11]/input[1]').click()


            time.sleep(1)


            listelements = driver.find_elements_by_xpath('//*[@id="historyTable"]/table/tbody/tr[1]/td[18]/a[1]')
            #//*[@id="historyTable"]/table/tbody/tr[2]/td[18]/a[1]
            if (len(listelements) > 0):

                 driver.find_element_by_xpath('//*[@id="historyTable"]/table/tbody/tr[1]/td[18]/a[1]').click()


                 time.sleep(1)
                 chat_id=driver.find_element_by_class_name('form-element').text
                 chat_id=chat_id.replace("#","")
                 chat_id=chat_id.replace("\n",'')
                 chat_id=chat_id.replace(":", "-")

                 fd = open(+chat_id+'.csv', 'a',encoding="utf-8")
                 # print("here"+fd)
                 fd.write(driver.find_element_by_id('messenger').text)


                 print(driver.find_element_by_id('messenger').text)



                 listvalues = driver.find_elements_by_class_name('value')

                 fd.write("\n------------------------------------------\n")
                 for each in listvalues:
                    print(each.text)
                    fd.write(each.text+"\n")

                 fd.close()

                 driver.find_element_by_id('cboxClose').click()





                 from google.cloud import storage

                 client = storage.Client()
                 bucket = client.get_bucket('callcenterchat')

                 blob = bucket.blob(chat_id+'.csv')
                 blob.upload_from_filename(chat_id+'.csv')
                 print("uploaded"++chat_id+'.csv')
                 os.remove(+chat_id+'.csv')



#//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[2]/a
#//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[1]/a
#//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[7]/a
callperday(driver,select,1,1,0,'2018-04-24')
driver.close()
callperday(driver,select,1,2,1)
callperday(driver,select,1,3,1)
callperday(driver,select,1,4,1)
callperday(driver,select,1,5,1)
callperday(driver,select,1,6,1)
callperday(driver,select,1,7,1)
callperday(driver,select,2,1,1)
callperday(driver,select,2,2,1)
callperday(driver,select,2,3,1)
callperday(driver,select,2,4,1)
callperday(driver,select,2,5,1)
callperday(driver,select,2,6,1)
callperday(driver,select,2,7,1)
callperday(driver,select,3,1,1)
callperday(driver,select,3,2,1)
callperday(driver,select,3,3,1)
callperday(driver,select,3,4,1)
callperday(driver,select,3,5,1)
callperday(driver,select,3,6,1)
callperday(driver,select,3,7,1)
callperday(driver,select,4,1,1)
callperday(driver,select,4,2,1)
callperday(driver,select,4,3,1)
callperday(driver,select,4,4,1)
callperday(driver,select,4,5,1)
callperday(driver,select,4,6,1)
callperday(driver,select,4,7,1)

driver.close()




