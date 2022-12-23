from selenium import webdriver
from selenium.webdriver.common.by import By
from pandas import DataFrame

browser = webdriver.Chrome(r'C:\Users\Андрей\Documents\chromdriver\chromedriver.exe')
browser.get('https://iotvega.com/product')
names =  browser.find_elements(By.CLASS_NAME, 'product-name')
names_array = []
for name in names:
    name_text =name.find_element(By.TAG_NAME,"h2").text
    names_array.append(name_text)
print(names_array)
df = DataFrame({'Product names': names_array})
df.to_excel('out.xlsx', sheet_name='sheet1', index=False)
