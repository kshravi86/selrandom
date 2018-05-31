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

time.sleep(3)

#https://gb1.gubagoo.com/chat_timeclock/index/summary
#https://gb1.gubagoo.com/chat_timeclock/index/summary?from=2018-05-16&to=2018-05-16&filter=1


from datetime import datetime, timedelta

timestr=datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

driver.get('https://gb1.gubagoo.com/chat_timeclock/index/summary?from='+timestr+'&to='+timestr+'&filter=1')
time.sleep(3)


driver.find_element_by_xpath('//*[@id="mini_popup_wrapper"]/input[2]').click()

time.sleep(1)

tablestr=driver.find_element(By.XPATH,'//*[@id="users-table"]')

alist=tablestr.find_elements(By.TAG_NAME,'a')

liststr=[]

for each in alist:
    liststr.append(each.get_attribute('href'))

fd = open('timeclock.csv', 'a')

fd.write('Operator,Date,Action,details\n')

fd.close()

for each in liststr:
    driver.get(each)

    driver.find_element_by_xpath('//*[@id="mini_popup_wrapper"]/input[2]').click()

    time.sleep(3)
    tbodystr=driver.find_element(By.XPATH,'//*[@id="users-table"]/tbody')

    trs = tbodystr.find_elements(By.TAG_NAME, 'tr')

    for every in trs:

        tds = every.find_elements(By.TAG_NAME, "td")
        for i in range(0, len(tds)):
            # print(i)
            if (i == 0):
                print(tds[i].get_attribute("innerHTML"))

                fd = open('timeclock.csv', 'a')
                fd.write(tds[i].get_attribute("innerHTML") + ",")
                fd.close()
            elif (i == 1):
                print(tds[i].get_attribute("innerHTML"))
                fd = open('timeclock.csv', 'a')
                tobewritten=str(tds[i].get_attribute("innerHTML"))
                tobewritten=tobewritten.replace(",","")
                fd.write(tobewritten + ",")
                fd.close()

            elif (i == 2):
                print(tds[i].get_attribute("innerHTML"))
                fd = open('timeclock.csv', 'a')
                fd.write(tds[i].get_attribute("innerHTML") + ",")
                fd.close()

            elif (i == 3):
                print(tds[i].get_attribute("innerHTML"))
                fd = open('timeclock.csv', 'a')
                fd.write(tds[i].get_attribute("innerHTML") + ",")
                fd.close()

            else:
                print("leave")
        fd=open('timeclock.csv','a')
        fd.write("\n")
        fd.close()

    fd=open('timeclock.csv','a')
    fd.write('\n\n\n')
    fd.close()




driver.close()