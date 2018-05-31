from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys




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

import csv

with open('user2.csv',encoding="utf-8") as csvfile:

        readCSV = csv.reader(csvfile, delimiter=',')

        for row in readCSV:
          try:
            selectstring=str(row[0])
            selectstring=selectstring.replace("\n",'')
            select.select_by_value(selectstring)
            time.sleep(3)

            driver.find_element_by_xpath('//*[@id="from"]').send_keys("sending")
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="from"]').clear()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="from"]').send_keys('2018-05-17')
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="from"]').send_keys(Keys.RETURN)

            driver.find_element_by_xpath('//*[@id="to"]').send_keys("sending")
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="to"]').clear()
            time.sleep(1)

            driver.find_element_by_xpath('//*[@id="to"]').send_keys('2018-05-17')

            driver.find_element_by_xpath('//*[@id="to"]').send_keys(Keys.RETURN)
            #//*[@id="historyTable"]/table/tbody
            driver.find_element_by_xpath('//*[@id="historyFilterForm"]/div[11]/input[1]').click()
            time.sleep(3)
            tablestr=driver.find_element(By.XPATH,'//*[@id="historyTable"]/table/tbody')
            atags=tablestr.find_elements(By.TAG_NAME,'a')
            setstr=set()
            for each in atags:
                attributestr=each.get_attribute('target')
                if(attributestr==None):
                    print("no")
                else:
                    if(each.text!='View chat' and each.text!='Send' and each.text!='View lead(s)'):


                      #print(each.text)
                      setstr.add(row[1]+","+each.text)

            for i in setstr:
              print(i)
              fd = open('mapper.csv', 'a')

              fd.write(i+"\n")
              fd.close()


          except Exception as e:
              print("some issue")

            #//*[@id="historyFilterForm"]/div[11]/input[1]
            #//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[2]/a
            #//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[3]/a

driver.close()