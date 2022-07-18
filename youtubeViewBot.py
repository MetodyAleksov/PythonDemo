from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

steam = webdriver.Chrome()
steam.get("https://store.steampowered.com/")

steam.implicitly_wait(30)

search = steam.find_element(By.ID,value="store_nav_search_term")
search.click()
search.send_keys("dead by daylight")

steam.implicitly_wait(30)

search.send_keys(Keys.ENTER)

steam.implicitly_wait(60)

game_link = steam.find_elements(By.TAG_NAME, 'a')[0]

print(game_link.get_attribute("href"))

#steam.close()