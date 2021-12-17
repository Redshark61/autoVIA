import time
import random
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# get the day number
day = date.today().day

# Get the first name, last name
firstname = input("Entre ton prénom : ")
lastname = input("Entre ton nom : ")

# The different choice for was was done during the week
choices = ["Cours", "Projet", "Cours", "Projet",
           "Cours", "Projet", "Dojo", "Projet", "Cours"]
random.seed(day)
# Randomize the list
random.shuffle(choices)

# Open the browser
driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeAITGeuVHTJUu79A7Fj0C0AMQUCxjZ2S0C2adZrgPFNihKBg/viewform")


# Get the body
body = driver.find_element_by_tag_name('body')
names = [firstname, lastname]

# Enter the name and firstname in the input
for i, name in zip(range(1, 3), names):
    inputField = driver.find_element_by_xpath(
        f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{i}]/div/div/div[2]/div/div[1]/div/div[1]/input')
    inputField.click()
    inputField.send_keys(name)

# Go to the next input
body.send_keys(Keys.TAB)
devPath = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/div[88]'
driver.switch_to.active_element.send_keys(Keys.ENTER)
# Wait for the dropdown to be visible
time.sleep(2)
inputField2 = driver.find_element_by_xpath(devPath)
inputField2.send_keys(Keys.ENTER)
time.sleep(2)

# Press esc key
body.send_keys(Keys.TAB)
currentDate = date.today()
currentDate = str(currentDate).split('-')[::-1]
print(currentDate)
elem = driver.switch_to.active_element
for i in currentDate:
    print(i)
    elem.send_keys(i)

body.send_keys(Keys.TAB)
for i in choices:
    elem = driver.switch_to.active_element
    elem.send_keys(i)
    elem.send_keys(Keys.TAB)

driver.switch_to.active_element.send_keys('Revue, retro')
driver.switch_to.active_element.send_keys(Keys.TAB)
for _ in range(2):
    driver.switch_to.active_element.send_keys('/')
    driver.switch_to.active_element.send_keys(Keys.TAB)

driver.switch_to.active_element.send_keys('tout')
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.send_keys('/')
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.click()
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.click()
driver.switch_to.active_element.send_keys(Keys.TAB)
driver.switch_to.active_element.click()

time.sleep(5)
driver.close()
