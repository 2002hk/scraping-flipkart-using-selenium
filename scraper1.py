import pandas as pd
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os
import json

## opening the file
with open('C:/Users/hrutu/Downloads/records.csv') as f:
    reader=csv.reader(f)
    data_read=[row for row in reader]
print(data_read)
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

filtered_data=[]
missing=0

#traversing rows form csv file
for i in range(0,len(data_read)):
    driver.get('https://www.flipkart.com/')
    search_box=driver.find_element("xpath",'//input[@class="Pke_EE"]')
    search_box.send_keys(data_read[i][0])
    search_box.send_keys(Keys.ENTER)
    time.sleep(4)
    #scrolling to the end
    driver.execute_script('window.scroll(0,document.body.scrollHeight)')
    # to extract total number of pages
    pages=driver.find_element("xpath",'//div[@class="_1G0WLw"]/child::span[1]').text
    print(pages)
    print(type(pages))
    #extracting the last element from the text
    no_of_pages=int(pages.split()[-1])
    print(no_of_pages)
    #looping through pages
    for j in range(1,no_of_pages+1):
        url=f'https://www.flipkart.com/search?q={data_read[i][0]}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={j}'
        driver.get(url)
        #xpath of all the product cards
        products=driver.find_elements("xpath",'//div[@class="slAVV4"]')
        #looping through each product in product cards
        for product in products:
            try:
                image=product.find_element("xpath",'.//img[@class="DByuf4"]').get_attribute('src')
                name=product.find_element("xpath",'.//a[@class="wjcEIp"]').text
                rating=product.find_element("xpath",'.//div[@class="XQDdHH"]').text
                price=product.find_element("xpath",'.//div[@class="Nx9bqj"]').text
                discount=product.find_element("xpath",'.//div[@class="UkUFwK"]').text

                filtered_data.append({
                    'Image_link':image,
                    'Name':name,
                    'Rating':rating,
                    'Price':price,
                    'Discount':discount
                })
            except Exception as e:
                missing+=1

#no of extracted data
print(len(filtered_data))
#no of missing data
print(missing)

# to csv
df=pd.DataFrame(filtered_data)
os.makedirs('output',exist_ok=True)
output_path='output/products2.csv'
df.to_csv(output_path,index=False)

#to json
with open("C:/Users/hrutu/Desktop/Flipkart Scraping/output/products2.json",'w') as f:
    json.dump(filtered_data,f)

driver.close()
driver.quit()