#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 00:43:13 2021

@author: macbookpro
"""
# The selenium module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# The BeautifulSoup module
from bs4 import BeautifulSoup


input_directory = str(input('Enter the directory of your choice where the files will be downloaded: '))
chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {'download.default_directory': input_directory})
    
# Install the Chrome Webdriver
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options= chromeOptions )

# Get the driver to the desired HTML markup and check by running an assertion on the text in the title of the page
driver.get("") #copy paste the website you want to automatically enter to


# Find the username box and enter the user's obtained username
username = driver.find_element_by_id("username") #Finds the element where you need to input your username and automate it
username.clear()
#input_username = str(input('Enter your Username: ')) #You can either input the username in the commamnd line or write it beforehand in the line below
username.send_keys('')

# Find the password box and enter the user's obtained password
password = driver.find_element_by_id("password")
password.clear()
#input_password = str(input('Enter your Password: '))
password.send_keys('')

# Submit the credentials by clicking the submit button
driver.find_element_by_class_name('btn').click()

# Wait for the page to load 
WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.LINK_TEXT, 'Business Analytics 2021')))

# Function that use BS4 to retrieve the content text to help the user choose the desired feature
def retrieve_list_of_content(class_source , tag):
    module_html = driver.page_source
    soup = BeautifulSoup(module_html, 'lxml')
    attributes = {'class': class_source}
    tag = soup.findAll(tag, attrs = attributes)
    content_list = [''.join(i.findAll(text=True)) for i in tag]
    return content_list

# List the modules available and display them in the command-line
list_of_modules = retrieve_list_of_content('subtitle break-long-words is-5 has-ellipsis-line-2 is-marginless' , 'h3')
list_of_css = ['#main-content > section:nth-child(3) > div > div > div > section > section.accordion.is-active.ProgrammesAccordion > div.accordion-body > div > div > div:nth-child('+ str(i) +') > div.card-content > a' for i in range(1,8)]

print('\n')
for number, module in enumerate(list_of_modules[:7]):
    print(number, module)
    
#input_class = int(input("Choose your module number: "))

# Select the desired module
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, list_of_css[3])))
element.click()
     
# Wait until the page load and select the link "Files"     
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.LINK_TEXT, 'Files')))
element.click()

# Wait for the page to load, switch to the parent frame and then switch to the first frame of the parent frame
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/section/div/div[2]/div/div/div/div/div/iframe')))
driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="main-content"]/section/div/div[2]/div/div/div/div/div/iframe'))
driver.switch_to.frame(0)

# Wait and use our function to list the available files and present them to the user
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.CSS_SELECTOR, '#embedded-app > div > div > div > div.dropins-previewer-content-container.dropins-previewer-content-container--no-footer > div > table > tbody > tr:nth-child(1)')))        
list_of_files = retrieve_list_of_content('mc-media-cell-text mc-media-cell-text-title', 'div')
list_of_css = ['#embedded-app > div > div > div > div.dropins-previewer-content-container.dropins-previewer-content-container--no-footer > div > table > tbody > tr:nth-child(' + str(i) + ')' for i in range(1,8)]

print('\n')
for number, file in enumerate(list_of_files):
    print(number, file)
                    
input_class = int(input("Choose your file number: "))

# Select the desired file
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, list_of_css[input_class])))
element.click()

# Wait for the file to load use our function to retrieve and list the content of the file
element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.CSS_SELECTOR, '#embedded-app > div > div > div > div.dropins-previewer-content-container.dropins-previewer-content-container--no-footer > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > div > div:nth-child(2) > button')))
list_of_content = retrieve_list_of_content('mc-media-cell-text mc-media-cell-text-title', 'div')
list_of_css = ['#embedded-app > div > div > div > div.dropins-previewer-content-container.dropins-previewer-content-container--no-footer > div > table > tbody > tr:nth-child('+ str(i) + ') > td:nth-child(2) > div > div:nth-child(2) > button' for i in range(1,20)]

print('\n')
for number, file in enumerate(list_of_content):
    print(number, file)

# Select the file to be downloaded in the directory of our choice 
input_class = int(input("Choose your the document number to download: "))
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, list_of_css[input_class])))
element.click()




