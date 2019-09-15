from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities().CHROME

caps["pageLoadStrategy"] = "none"  #  interactive

start_time = time.time()

browser = webdriver.Chrome('C:\\Users\\Colin Hebert\\Downloads\\chromedriver')



alphabet = "abcdefghijklmnopqrstuvwxyz"
#browser.get("http://my.lsu.edu/")
#time.sleep(20)
#browser.get("https://sso.paws.lsu.edu/ltpatoken_creator/createLtpaToken.action?return_url=http://appl103.LSU.EDU/DIR003.nsf")
browser.get("https://appl103.lsu.edu/dir003.nsf/people+by+name?openform")

def getElement(elemType, elemName):
    if elemType == "NAME":
        return WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.NAME, elemName)))
    if elemType == "ID":
        return WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.ID, elemName)))
    if elemType == "CSS":
        return WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, elemName)))

for letter1 in alphabet:
    for letter2 in alphabet:
        select = Select(getElement("NAME", "LastOper"))
        select.select_by_visible_text("begins with")
        select = Select(getElement("NAME", "FirstOper"))
        select.select_by_visible_text("begins with")

        name = getElement("NAME", "LastName")
        name.clear()
        name.send_keys(letter1)

        name = getElement("NAME", "FirstName")
        name.clear()
        name.send_keys(letter2)

        browser.find_element_by_name("ButtonChoice").click()
        WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p")))
        str = browser.find_element_by_css_selector("p").text
        if "No names found" not in str:
            links = browser.find_element_by_xpath("//table[3]").find_elements_by_css_selector("a")
            for b in links:
                b.click()
                #print(b.get_attribute("href"))
                print(browser.find_element_by_css_selector("p").text)

print(time.time() - start_time)

