from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pynput.keyboard import Key,Controller
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import csv

#browser=webdriver.Firefox()
driver = webdriver.Firefox()
#driver = webdriver.Firefox(executable_path="C:\\Users\\sushj\\Desktop\\geckodriver.exe")
driver.get("https://www.zomato.com ")

elm = driver.find_element_by_xpath('//input[@class="location prompt fontsize2"]')
elm.click()
time.sleep(2)

elm.send_keys("pune")

#driver.get("https://www.zomato.com/pune")


element = driver.find_element_by_xpath('//input[@id="keywords_input"]')

element.click()
time.sleep(3)
element.send_keys("McDonald's")
time.sleep(3)

element.send_keys(Keys.DOWN)
time.sleep(3)

element.send_keys(Keys.ENTER)
time.sleep(3)

print(driver.current_url)
currentUrl = driver.current_url

driver.get(currentUrl)

McDonald_links = driver.find_elements_by_partial_link_text("McDonald's")

with open(r"C:\Users\hp\Desktop\MacdonaldData.csv",'w') as csvfile:
    fieldnamessss = ['Name','Phone No','Address','Reviewer Name','Reviewer Score','Reviewer Text','Link']
    writer = csv.DictWriter(csvfile,fieldnames = fieldnamessss)
    writer.writeheader()
    i = 0
    j = 1
    for x in range(28):
    #for McDonald_link in McDonald_links:
        
        McDonald_link_list = driver.find_elements_by_partial_link_text("McDonald's") #Intializing the list again on every page load/navigation to prevent StaleElementReferenceException
        print(McDonald_link_list[i])
        McDonald_link_list[i].click()     
        currentUrl = driver.current_url
        driver.get(currentUrl)
        #browser.get(currentUrl)
        time.sleep(5)

        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<< Printing Macdonal's "+str(x+1)+" data starts>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        html=driver.page_source
        soup=BeautifulSoup(html)

        name=soup.find("a", class_="ui large header left")
        if name is None:
            name = ""
        else:
            name= name.get_text().strip()
        print("Name : "+name)

        phone=soup.find("span", class_="tel")
        if phone is None:
            phone = ""
        else:
            phone= phone.get_text().strip()
        print("Phone no : "+phone)

        address=soup.find("div", class_="resinfo-icon")
        if address is None:
            address = ""
        else:
            address= address.get_text().strip()
        print("Address : "+address)

        reviewerName=soup.find("div", class_="header nowrap ui left")
        if reviewerName is None:
            reviewerName = ""
        else:
            reviewerName= reviewerName.get_text().strip()
        try:
            print("Reviewer Name : "+reviewerName)
        except:
            reviewerName=""
            print("Unicode is used in review Name")    

        score=soup.find("div", class_="ttupper fs12px left bold zdhl2 tooltip icon-font-level-1")
        if score is None:
            score = ""
        else:    
            score= score.get('aria-label')  
        print("Score : "+score)

        reviewTextParent=soup.find("div", class_="res-review-body")
        reviewText = reviewTextParent.find("div", class_="ttupper")
        if reviewText is None:
            reviewText = ""
        else:
            reviewText= reviewText.next_sibling.strip()
        try:
            print("Review Text : "+reviewText).encode('utf-8')
        except:
            reviewText=""
            print("Unicode is used in review text")

        print("Link : "+currentUrl)
        
        #Writing into the csv file
        writer.writerow({'Name':name,'Phone No':phone,'Address':address,'Reviewer Name': reviewerName,'Reviewer Score':score,'Reviewer Text':reviewText,'Link':currentUrl})

        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<< Printing data ends>>>>>>>>>>>>>>>>>>>>>>>>>>>")
           
        driver.back() # Going back to previous page
        time.sleep(7)
        currentUrl = driver.current_url
        driver.get(currentUrl)
        i = i + 1
        if i == 13:
            i=0
            j=j+1
            url = "/pune/restaurants/mcdonalds?page="+str(j)
            page_link = driver.find_element_by_xpath('//a[@href="'+url+'"]')
            page_link.click()
            currentUrl = driver.current_url
            print(currentUrl)
            driver.get(currentUrl)

