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

driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/ul/li[3]/a').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="wrapper"]/div[1]/ul/li[4]/a').click()

time.sleep(9)

try:
    element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="stats-box"]/ul/li[3]/a'))
    )
finally:
    print('leave')


element.click()


time.sleep(10)

from selenium.webdriver.common.by import By

divname=driver.find_element(By.ID,"operators_report_tab")

table = divname.find_element(By.TAG_NAME, 'tbody')

trs=table.find_elements(By.TAG_NAME,'tr')

print(len(trs))

count=0
fd = open('opearatorstats.csv', 'a')

#fd.write(table.text)

fd.write('Operator,Chats,Leads,Appointments,Avg Chat Duration,Suspended w/ Lead,Avg Response Time,Avg Customer Rating,Avg System Rating,Conversion,Chats,Leads\n')


for every in trs:


     tds=every.find_elements(By.TAG_NAME,"td")
     for i in range(0,len(tds)):
         #print(i)
         if(i==0):

             print(tds[i].get_attribute("innerHTML"))

             fd.write(tds[i].get_attribute("innerHTML")+",")
         elif(i==1):
             atag=tds[i].find_element(By.TAG_NAME,'a')
             print(atag.get_attribute("innerHTML"))
             fd.write(atag.get_attribute("innerHTML")+",")
         elif (i == 2):
             atag = tds[i].find_element(By.TAG_NAME, 'a')
             print(atag.get_attribute("innerHTML"))
             fd.write(atag.get_attribute("innerHTML") + ",")
         elif(i==3):
             atag = tds[i].find_element(By.TAG_NAME, 'a')
             print(atag.get_attribute("innerHTML"))
             fd.write(atag.get_attribute("innerHTML") + ",")
         elif(i==4):
             content = str(tds[i].get_attribute("innerHTML"))
             print(tds[i].get_attribute("innerHTML"))
             fd.write(tds[i].get_attribute("innerHTML")+",")
         elif (i == 5):
             atag = tds[i].find_element(By.TAG_NAME, 'a')
             print(atag.get_attribute("innerHTML"))
             fd.write(atag.get_attribute("innerHTML") + ",")
         elif(i==6):

             print(tds[i].get_attribute("innerHTML"))

             fd.write(tds[i].get_attribute("innerHTML")+",")

         elif(i==7):
             spantag=tds[i].find_elements(By.TAG_NAME,'span')
             print(spantag[1].get_attribute("innerHTML"))
             fd.write(spantag[1].get_attribute("innerHTML")+",")

         elif (i == 8):
             spantag=tds[i].find_elements(By.TAG_NAME,'span')
             print(spantag[1].get_attribute("innerHTML"))
             fd.write(spantag[1].get_attribute("innerHTML")+",")
         elif(i==9):
             print(tds[i].get_attribute("innerHTML"))

             fd.write(tds[i].get_attribute("innerHTML") + ",")
         elif(i==10):
             print(tds[i].get_attribute("innerHTML"))

             fd.write(tds[i].get_attribute("innerHTML") + ",")
         elif (i == 11):
             print(tds[i].get_attribute("innerHTML"))

             fd.write(tds[i].get_attribute("innerHTML") + ",")

         else:
             print("leave")

     fd.write("\n")


fd.close()

#driver.find_element_by_xpath('//*[@id="stats-box"]/ul/li[3]/a').click()

#//*[@id="stats-box"]/ul/li[3]/a

#//*[@id="changelist"]/table/tbody/tr[1]/td[4]

time.sleep(3)

driver.close()