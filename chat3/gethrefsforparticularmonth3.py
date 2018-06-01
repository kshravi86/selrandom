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

#driver.find_element_by_xpath('//*[@id="historyFilterForm"]/div[11]/input[1]').click()



# name of my select filter_account_id
#//*[@id="operator_id"]
time.sleep(3)




import csv

with open('User.csv',encoding="utf-8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        for row in readCSV:
            #Abhishek.K (Abhishek Kattamreddi)
            try:
             select = Select(driver.find_element_by_id('operator_id'))
             print(row[2]+" "+"("+row[1]+")")
             select.select_by_visible_text(row[2]+" "+"("+row[1]+")")
             #time.sleep(1)
             driver.find_element_by_xpath('//*[@id="from"]').send_keys("sending")
             #time.sleep(1)
             driver.find_element_by_xpath('//*[@id="from"]').clear()
             #time.sleep(1)
             driver.find_element_by_xpath('//*[@id="from"]').send_keys("2018-05-24")
             #time.sleep(1)
             driver.find_element_by_xpath('//*[@id="from"]').send_keys(Keys.RETURN)

             driver.find_element_by_xpath('//*[@id="to"]').send_keys("sending")
             #time.sleep(1)
             driver.find_element_by_xpath('//*[@id="to"]').clear()
             #time.sleep(1)

             driver.find_element_by_xpath('//*[@id="to"]').send_keys("2018-05-24")

             driver.find_element_by_xpath('//*[@id="to"]').send_keys(Keys.RETURN)

             driver.find_element_by_xpath('//*[@id="historyFilterForm"]/div[11]/input[1]').click()
             count = 0
             time.sleep(1)
             tablevalues=driver.find_element(By.XPATH,'//*[@id="historyTable"]/div/span')
             atagvalues=tablevalues.find_elements(By.TAG_NAME,'a')
             listvalues=[]
             for each in atagvalues:
                 print(each.get_attribute('href'))
                 listvalues.append(each.get_attribute('href'))

             for each in listvalues:
                driver.get(each)
                table = driver.find_element_by_xpath('//*[@id="historyTable"]/table/tbody')
                atags = table.find_elements(By.TAG_NAME, 'a')
                listforatags=[]
                for every in atags:
                    listinside=[]
                    listinside.append(every.get_attribute('class'))
                    listinside.append(every.get_attribute('href'))

                    listforatags.append(listinside)
                for one in listforatags:
                    if(one[0]=='view-link colorbox cboxElement'):
                        count = count + 1
                        fd = open('hrefs3.csv', 'a')
                        print(one[1])
                        fd.write(one[1] + "\n")
                        fd.close()








            except Exception as e:
                print("not found")
                print(e)
                #select.select_by_visible_text(row[2] + " " + "(" + row[1] + " )")







import time

time.sleep(1)

driver.find_element_by_xpath('//*[@id="historyFilterForm"]/div[11]/input[1]').click()



def callperday(driver):



    count=0

    for i in range(1,25):

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
            fd = open('hrefs3.csv', 'a')

            fd.write(each.get_attribute('href') + "\n")
            fd.close()


time.sleep(5)
#callperday(driver)
