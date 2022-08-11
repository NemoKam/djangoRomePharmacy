from selenium import webdriver
from bs4 import BeautifulSoup
import time
lefttop = [42.0365919,12.3535348]
tobot = 0.02647399*10/15
toright = 0.03624632
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x935')
driver = webdriver.Chrome('chromedriver.exe',chrome_options=options)
f = open('all2.txt','w')
for q in range(1,16):
    for j in range(1,11):
        ll = f'{round(lefttop[0]-float(tobot)*float(q),10)},{round(lefttop[1]+float(toright)*float(j),10)}'
        print(q,j,ll)
        url = f'https://www.google.com/maps/search/pharmacy+rome/@{ll},15z/'
        driver.get(url)
        how = 0
        while True:
            try:
                time.sleep(1)
                driver.execute_script(f'document.querySelectorAll(".Nv2PK")[{how}].scrollIntoView()')
                how+=1
            except:
                try:
                    time.sleep(10)
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
                f.write(f'{name}\n{url}\n{comms}\n')
            except:
                pass
f.close()