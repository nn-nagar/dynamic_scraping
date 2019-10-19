from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pynput.keyboard import Key,Controller
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import csv

driver = webdriver.Firefox()
driver.get("https://meetinglibrary.asco.org/record/148853/abstract")


time.sleep(5)
#ascoLinks = driver.find_element_by_xpath('//div[@class="category ng-star-inserted"]')

time.sleep(2)
with open(r"C:\Users\hp\Desktop\AscoData.csv",'w') as csvfile:
    fieldnamessss = ['Title','Author','Medical Center']
    writer = csv.DictWriter(csvfile,fieldnames = fieldnamessss)
    writer.writeheader()
    # ascoLink_list = driver.find_element_by_xpath('//div[@class="category ng-star-inserted"]')
    # ascoLink_list.click()
    # #element.click()
    time.sleep(2)
    

    html=driver.page_source
    soup=BeautifulSoup(html)

    currentUrl = driver.current_url
    driver.get(currentUrl)
    time.sleep(2)


    name=soup.find("h1", class_="ng-tns-c9-2")
    if name is None:
        name = ""
    else:
        name= name.get_text().strip()
    print("Title : "+name)

    author=soup.find("div", class_="authors")
    if author is None:
        author = ""
    else:
        author= author.get_text().strip()

    print("Auther : "+author)

    medicalCenter=soup.find("div", class_="authors")
    if medicalCenter is None:
        medicalCenter = ""
    else:
        medicalCenter= medicalCenter.get_text().strip()
    print("MedicalCenter : "+medicalCenter)


    print("Link : "+currentUrl)

    writer.writerow({'Title':name,'Author': author,'Medical Center': medicalCenter})
    # driver.back() # Going back to previous page
    #     #time.sleep(7)
    #     currentUrl = driver.current_url
    #     driver.get(currentUrl)
        
        
       

    # # author=soup.find("div", class_="authors")
    # # if author is None:
    # #     author = ""
    # # else:
    # #     author= author.get_text().strip()
    # #     #auther = 
    # # print("Auther : "+author)



 

