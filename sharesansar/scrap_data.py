from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()
driver.get('https://www.sharesansar.com/existing-issues')

table_element = driver.find_element(By.ID, 'myTableEip')
row_elements = table_element.find_elements(By.TAG_NAME, 'tr')

table_data = []

for row in row_elements[1:]:
    data_elements = row.find_elements(By.TAG_NAME, 'td')
    # for data in data_elements:
    #     print(data.text)

    ipo = {
        'S.N': data_elements[0].text,
        'Symbol': data_elements[1].text,
        'Company': data_elements[2].text,
        'Unit': data_elements[3].text
    }

    table_data.append(ipo)

with open('ipo_data.json', 'w') as f:
    json.dump(table_data, f, indent=2)

driver.close()