from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time


from selenium import webdriver
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# Google Chrome
driver = webdriver.Chrome('/Users/aakashravi/PycharmProjects/callcenterautomation/chromedriver')

# ------------------------------
# The actual test scenario: Test the codepad.org code execution service.

# Go to codepad.org
driver.get('https://gb1.gubagoo.com/micro/cc/index.php#')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('flatworld1@gubagoo.com')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()


time.sleep(3)

try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
    )
finally:
    print('leave')

element.send_keys('Flatworld123')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
time.sleep(3)


driver.find_element_by_xpath('//*[@id="mode-chats"]').click()

time.sleep(3)

def action_taking(driver,number_str):


 select = Select(driver.find_element_by_xpath('//*[@id="op-groups"]'))


# select by value
 select.select_by_value('Flat World')

 time.sleep(3)

 driver.find_element_by_xpath('//*[@id="yesterday"]').click()

 time.sleep(3)
 if(number_str!=1):
  driver.find_element_by_xpath('//*[@id="grid"]/div[3]/div/span['+str(number_str)+']/a').click()
  time.sleep(3)


 from selenium.webdriver.common.by import By

 trs = driver.find_elements(By.TAG_NAME, "tr")

 print(len(trs))

 count=0
 fd = open('suspectchatfinal.csv', 'a',encoding="utf-8")

 for every in trs:

    if(count==0):
        count=count+1
        ths = every.find_elements(By.TAG_NAME, "th")
        for each in ths:
            if(len(each.text)>0):
              print(each.text,end=',')
              cleantext=str(each.text)
              cleantext=cleantext.replace("\n","")
              fd.write(cleantext+",")
        print("")
        fd.write("\n")
    else:
     tds=every.find_elements(By.TAG_NAME,"td")
     count=0
     for each in tds:

         if (len(each.text) > 0):
             print(each.text, end=',')

             cleantext = str(each.text)
             cleantext = cleantext.replace("\n", "")
             if(count==5):
               index=cleantext.find('s')
               if(index!=-1):
                   fd.write(cleantext[0:index]+","+cleantext[index+1:]+",")
               else:
                   fd.write(cleantext)
             else:
              fd.write(cleantext + ",")

         count=count+1

     fd.write("\n")



 fd.close()

#//*[@id="grid"]/div[3]/div/span[2]/a
try:

 action_taking(driver,1)

 action_taking(driver,2)


 action_taking(driver,3)

 action_taking(driver,4)

 action_taking(driver,5)

 action_taking(driver,6)

 action_taking(driver,7)


 action_taking(driver,8)

 action_taking(driver,9)


 action_taking(driver,10)

 action_taking(driver,11)

 action_taking(driver,12)

 action_taking(driver,13)

 action_taking(driver,14)


 action_taking(driver,15)

except:
    print("exception happened")




driver.close()





