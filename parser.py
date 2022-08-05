# -*- coding: utf-8 -*-
# parser
import psycopg2
from selenium import webdriver
from bs4 import BeautifulSoup
import time
conn = psycopg2.connect(
    host="localhost",
    database="pharmacy",
    user="kamil",
    password="hduaos82g37x02",
    port=5432) 
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x935')
driver = webdriver.Chrome('chromedriver.exe',chrome_options=options)
driver.get('https://www.google.com/maps/search/%D0%B0%D0%BF%D1%82%D0%B5%D0%BA%D0%B8+%D0%B2+%D0%A0%D0%B8%D0%BC,+%D0%98%D1%82%D0%B0%D0%BB%D0%B8%D1%8F/')
how = 0
pharmacy = []
while True:
    try:
        time.sleep(1)
        driver.execute_script(f'document.querySelectorAll(".Nv2PK")[{how}].scrollIntoView()')
        how+=1
    except:
        break
soup = BeautifulSoup(driver.page_source,'html.parser')
for i in soup.findAll('div',{'class':'Nv2PK'}):
    try:
        comms = int(i.find('span',{'class':'UY7F9'}).text.replace('(','').replace(')',''))
        name = i.find('a',{'class':'hfpxzc'})['aria-label'] 
        url = i.find('a',{'class':'hfpxzc'})['href']
        pharmacy.append([name,url,comms])
    except:
        pass
for j in range(len(pharmacy)):
    driver.get(pharmacy[j][1])
    time.sleep(1)
    driver.find_element_by_css_selector('.DkEaL').click()
    time.sleep(13)
    i = 0
    ii = 1
    cursor = conn.cursor()
    if pharmacy[j][2]!=0:
        for q in range(pharmacy[j][2]): 
            time.sleep(1)
            try:
                element = driver.execute_script(f'document.querySelectorAll(".jftiEf")[{i}].scrollIntoView();')
                time.sleep(2)
            except:
                element = driver.execute_script('document.querySelector(".DxyBCb").scrollTop=21000000000;')
                time.sleep(10)
            name = driver.find_elements_by_css_selector('.d4r55 > span')[i].text
            date = driver.find_elements_by_css_selector('.rsqaWe')[i].text
            try:
                driver.find_element_by_xpath(f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[10]/div[{ii}]/div/div[3]/div[4]/jsl/button').click()
                time.sleep(1)
            except:
                pass
            try:
                text = driver.find_elements_by_css_selector('.jftiEf .wiI7pd')[i].text.split('(Оригинал)\n')[1]
            except:
                text = ''
            i+=1
            ii+=3
            cursor.execute("INSERT INTO comms_comment (pharmacyurl, pharmacyname, author, sources, date, text) VALUES(%s, %s, %s, %s, %s, %s)", (pharmacy[j][1], pharmacy[j][0], name, pharmacy[j][1], date , text))
            conn.commit()
    print(pharmacy[j][0])
print('Все')
driver.quit()

