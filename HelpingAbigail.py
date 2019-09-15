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

browser = webdriver.Chrome(r"C:\Users\Colin Hebert\Downloads\chromedriver_win32\chromedriver.exe")

url = "https://www.google.com/forms/about/"

print("Please sign into your google account.")
print("The program will start once you open a new Google form.")

browser.get(url)

while browser.current_url[0:len("https://docs.google.com/forms/d/")] != "https://docs.google.com/forms/d/":
    time.sleep(1)
print("Great, now you can sit back and just look pretty (as always).")


def get_elements(elemType, elemName):
    if elemType == "NAME":
        return WebDriverWait(browser, 100).until(
            EC.presence_of_all_elements_located((By.NAME, elemName)))
    if elemType == "ID":
        return WebDriverWait(browser, 100).until(
            EC.presence_of_all_elements_located((By.ID, elemName)))
    if elemType == "CLASS":
        return WebDriverWait(browser, 100).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, elemName)))
    if elemType == "XPATH":
        return WebDriverWait(browser, 100).until(
            EC.presence_of_all_elements_located((By.XPATH, elemName)))

in_counter = 0
txt_counter = 1

# select = Select(get_element("CSS", "input"))
elems = get_elements("XPATH", "//*[@jsname = 'YPqjbf']")
textareas = get_elements("CSS", "textarea")
elems[in_counter].clear()
elems[in_counter].send_keys("Sorority Form")
in_counter = 2
#textareas[txt_counter].clear()
#textareas[txt_counter].send_keys("Yeet")

names = ["Colin Hebert", "Colin G Hebert", "Colin Greg Hebert", "Colin Gregory Hebert"]

for name in names:
    in_counter += 3
    #textareas[txt_counter].clear()
    #textareas[txt_counter].send_keys(name)
    #elems[in_counter].click()
    print(elems[in_counter].text)
    browser.find_elements_by_xpath("//*[@jsname = 'YPqjbf']")[5].send_keys(name)
    in_counter += 3
    browser.find_elements_by_xpath("//*[@jsname = 'YPqjbf']")[8].send_keys(name)
    in_counter += 1
    browser.find_elements_by_xpath("//*[@jsname = 'YPqjbf']")[9].send_keys(name)
    in_counter += 1
    browser.find_elements_by_xpath("//*[@jsname = 'YPqjbf']")[10].send_keys(name)


