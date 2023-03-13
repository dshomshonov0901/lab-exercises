#!/usr/bin/env python
# coding: utf-8

# In[10]:





# In[43]:


from selenium import webdriver
import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = Service(r"C:\Users\Daniella\Favorites\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

driver.get("https://www.binghamton-ny.gov/home")
government = driver.find_element(By.XPATH, '//*[@id="dropdownrootitem3"]/a')
submenu_departments = driver.find_element(By.XPATH, "//*[@id='dropdownrootitem3']/div/div/ul[1]/li/a")

actions = ActionChains(driver)
actions.move_to_element(government)
actions.click(government)
actions.click(submenu_departments)
actions.perform()

try:
        civil = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="widget_4_33_127"]/ul/li[16]/a')))
        civil.click()
        employment = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="leftNav_1038_0_145"]/ul/li/ul/li[14]/ul/li/a')))
        employment.click()
        
            
        with open("table.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Job", "                       Type", "        Deadline", "      Salary"])
            
            r= 1
 
        # Obtain the number of columns in table
            p= 1
 
        # Print rows and columns
            while r<15:
                    job = driver.find_element(By.XPATH, '//*[@id="ColumnUserControl4"]/div[2]/table/tbody/tr['+str(r)+']/td[1]').text 
                    job_type = driver.find_element(By.XPATH, '//*[@id="ColumnUserControl4"]/div[2]/table/tbody/tr['+str(r)+']/td[2]').text
                    deadline = driver.find_element(By.XPATH, '//*[@id="ColumnUserControl4"]/div[2]/table/tbody/tr['+str(r)+']/td[3]').text 
                    salary = driver.find_element(By.XPATH, '//*[@id="ColumnUserControl4"]/div[2]/table/tbody/tr['+str(r)+']/td[4]').text 
                    writer.writerow([job, job_type, deadline, salary])
                    r+=1
            
    
finally:
    driver.quit()


# In[ ]:




