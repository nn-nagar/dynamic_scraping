# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
from pynput.keyboard import Key,Controller
# from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import csv
import requests

#browser=webdriver.Firefox()
# driver = webdriver.Firefox()
#driver = webdriver.Firefox(executable_path="C:\\Users\\sushj\\Desktop\\geckodriver.exe")
page = requests.get("https://meetinglibrary.asco.org/record/148853/abstract")

# elm = driver.find_element_by_xpath('//input[@class="location prompt fontsize2"]')
# elm.click()
# time.sleep(2)

# elm.send_keys("pune")

#driver.get("https://www.zomato.com/pune")
time.sleep(2)

#print("<<<<<<<<<<<<<<<<<<<<<<<<<<<< Printing Macdonal's "+str(x+1)+" data starts>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(page.status_code)
soup = BeautifulSoup(page.text, 'html.parser')

#print(soup.encode('utf-8'))
title = soup.title.text
print('Title : ',title)

name = soup.find("h1", class_="ng-tns-c9-2")

#for name in names:
name = name.text.strip()
# if name is None:
#     name = ""
# else:
#name = str(name.text.strip())
print("Name : "+name)
with open(r"AscoData.csv",'w') as csvfile:
    fieldnamessss = ['Title','Author','Medical Center']
    writer = csv.DictWriter(csvfile,fieldnames = fieldnamessss)
    writer.writeheader()
    # ascoLink_list = driver.find_element_by_xpath('//div[@class="category ng-star-inserted"]')
    # ascoLink_list.click()
    # #element.click()
    time.sleep(2)
    currentUrl = driver.current_url
    driver.get(currentUrl)
    time.sleep(2)


    print(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')

    #print(soup.encode('utf-8'))
    title = soup.title.text
    print('Title : ',title)

    name = soup.find_all("h1", class_="ng-tns-c9-2")

    #for name in names:
    name = name.text.strip()
# 
    author=soup.find_all("div", class_="authors")
    if author is None:
        author = ""
    else:
        author= author.get_text().strip()

    print("Auther : "+author)

    medicalCenter=soup.find_all("div", class_="authors")
    if medicalCenter is None:
        medicalCenter = ""
    else:
        medicalCenter= medicalCenter.get_text().strip()
    print("MedicalCenter : "+medicalCenter)


    print("Link : "+currentUrl)

    writer.writerow({'Title':name,'Author': author,'Medical Center': medicalCenter})

 

