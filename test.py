from selenium import webdriver
import time
from time import sleep

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.flipkart.com/")
driver.find_element_by_xpath("//input[@class='_2IX_2- VJZDxU']").send_keys("7702012703")
driver.find_element_by_xpath("//input[@class='_2IX_2- _3mctLh VJZDxU']").send_keys("amulya@12345")
driver.find_element_by_xpath("//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click


