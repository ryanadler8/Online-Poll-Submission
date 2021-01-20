from selenium import webdriver
import chromedriver_autoinstaller
import time
import pandas as pd
import random


xl = pd.ExcelFile(FILE_PATH)
df = xl.parse('Sheet1') 


for index, row in df.iterrows():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get(WEBADDRESS)
    time.sleep(3)
    
    yourname = driver.find_element_by_id(ID_NAME_1)
    time.sleep(3)
    yourname.send_keys(row[COLUMN_NAME_1])

    emailid = driver.find_element_by_id(ID_NAME_2)
    time.sleep(2)
    emailid.send_keys(row[COLUMN_NAME_2])
    
    WinningTeam = ['Knicks','Islanders','Knicks','Knicks']
    
    firstpick = random.choice(WinningTeam)
    firstpickline = driver.find_element_by_id(ID_NAME_3)
    time.sleep(2)
    firstpickline.send_keys(firstpick)
    
    RestofTeams = ['Jets', 'Giants', 'Nets', 'Rangers', 'Mets', 'Yankees']
    
    secondpick = random.choice(RestofTeams)
    secondpickline = driver.find_element_by_id(ID_NAME_4)
    time.sleep(2)
    secondpickline.send_keys(secondpick)
    RestofTeams.remove(secondpick)
    
    thirdpick = random.choice(RestofTeams)
    thirdpickline = driver.find_element_by_id(ID_NAME_5)
    time.sleep(2)
    thirdpickline.send_keys(thirdpick)
    RestofTeams.remove(thirdpick)
    
    fourthpick = random.choice(RestofTeams)
    fourthpickline = driver.find_element_by_id(ID_NAME_6)
    time.sleep(2)
    fourthpickline.send_keys(fourthpick)
    RestofTeams.remove(fourthpick)
    
    fifthpick = random.choice(RestofTeams)
    fifthpickline = driver.find_element_by_id(ID_NAME_7)
    time.sleep(2)
    fifthpickline.send_keys(fifthpick)
    RestofTeams.remove(fifthpick)
    
    submit = driver.find_element_by_class_name(SUBMIT_BUTTON)
    submit.click()
    print(row['Full Name'],row['Full email'],firstpick,secondpick,thirdpick,fourthpick)
    time.sleep(3)
    driver.close()
    time.sleep(15)
    
    
