from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities().CHROME

caps["pageLoadStrategy"] = "none"  #  interactive

start_time = time.time()
browser = webdriver.Chrome('C:\\Users\\Colin Hebert\\Downloads\\chromedriver')

cardNum = "4320045897241022"
exp = "09/21"
cvv = "129"
email = "yeetboi@gmail.com"
firstName = "Abraham"
lastName = "Lincoln"
address = "4646 Loyola Dr."
city = "Baton Rouge"
zip = "70808"
phone = "2255551212"

browser.get("https://kith.com/collections/kith-monday-program")
browser.get("https://kith.com/collections/kith-monday-program/products/kith-x-tommy-hilfiger-crest-beanie-burgundy")
elem = WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.NAME, "add")))
time.sleep(0.5)
elem.click()
#browser.find_element_by_name("add").click()
#time.sleep(3)
WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.NAME, "checkout"))).click()
#browser.find_element_by_name("checkout").click()
WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.NAME, "checkout[email]"))).send_keys(email)
#browser.find_element_by_name("checkout[email]").send_keys(email)
WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.NAME, "checkout[shipping_address][first_name]"))).send_keys(firstName)
#browser.find_element_by_name("checkout[shipping_address][first_name]").send_keys(firstName)
WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.NAME, "checkout[shipping_address][last_name]"))).send_keys(lastName)
#browser.find_element_by_name("checkout[shipping_address][last_name]").send_keys(lastName)
WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.NAME, "checkout[shipping_address][address1]"))).send_keys(address)
#browser.find_element_by_name("checkout[shipping_address][address1]").send_keys(address)
WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.NAME, "checkout[shipping_address][city]"))).send_keys(city)
#browser.find_element_by_name("checkout[shipping_address][city]").send_keys(city)
WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.NAME, "checkout[shipping_address][zip]"))).send_keys(zip)
#browser.find_element_by_name("checkout[shipping_address][zip]").send_keys(zip)
WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.NAME, "checkout[shipping_address][phone]"))).send_keys(phone)
#browser.find_element_by_name("checkout[shipping_address][phone]").send_keys(phone)
WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.NAME, "button"))).click()
time.sleep(0.5)
WebDriverWait(browser, 100).until(
    EC.presence_of_element_located((By.NAME, "button"))).click()
#browser.find_element_by_name("button").click()
#browser.find_element_by_name("button").click()
time.sleep(7)
iframes = browser.find_elements_by_class_name("card-fields-iframe")
browser.switch_to.frame(iframes[1])
browser.find_element_by_css_selector("input").send_keys(cardNum)
browser.switch_to.default_content()
browser.switch_to.frame(iframes[1])

browser.find_element_by_css_selector("input").click().send_keys(firstName + " " + lastName)
browser.switch_to.frame(iframes[2])
browser.find_element_by_css_selector("input").send_keys(exp)
browser.switch_to.frame(iframes[3])
browser.find_element_by_css_selector("input").send_keys(cvv)

# time.sleep(10)
# browser.close()

# /collections/kith-monday-program/products/kith-x-boyz-in-the-hood-hoodie-white
