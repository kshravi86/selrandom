from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time




# Google Chrome
driver = webdriver.Chrome('/Users/aakashravi/PycharmProjects/callcenterautomation/chromedriver3')

# ------------------------------
# The actual test scenario: Test the codepad.org code execution service.

# Go to codepad.org
driver.get('https://gb1.gubagoo.com/micro/cc/index.php#')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('flatworld1@gubagoo.com')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()


time.sleep(3)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Flatworld123')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
time.sleep(3)


driver.find_element_by_xpath('//*[@id="mode-ops"]').click()

time.sleep(3)


driver.find_element_by_xpath('//*[@id="agent-yesterday"]').click()

time.sleep(3)

divname=driver.find_element_by_xpath('//*[@id="grid"]/div[2]')

table=divname.find_element(By.TAG_NAME,'tbody')



fd = open('suspectchatoperators.csv', 'a')



trs=table.find_elements(By.TAG_NAME,'tr')

fd.write('\n')
for every in trs:


     tds=every.find_elements(By.TAG_NAME,"td")
     for i in range(0,len(tds)):
         #print(i)
         if(i==0):
             try:
                atag = tds[i].find_element(By.TAG_NAME, 'a')
                print(atag.get_attribute("innerHTML"))
                fd.write(atag.get_attribute("innerHTML") + ",")
             except:
                 print('no opearators')

         else:

             print(tds[i].get_attribute("innerHTML"))

             fd.write(tds[i].get_attribute("innerHTML")+",")

     fd.write("\n")


fd.close()

#driver.find_element_by_xpath('//*[@id="stats-box"]/ul/li[3]/a').click()

#//*[@id="stats-box"]/ul/li[3]/a

#//*[@id="changelist"]/table/tbody/tr[1]/td[4]

time.sleep(3)

driver.close()

#fd.write(table.text)








