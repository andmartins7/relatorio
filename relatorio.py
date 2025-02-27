from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
import time
import os
import sys

options = Options()
options.headless = True
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.download.folderList",2)
firefox_profile.set_preference("browser.download.manager.showWhenStarting", False)
firefox_profile.set_preference("browser.download.dir", os.getcwd())
firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv; charset=ISO-8859-1")

browser = webdriver.Firefox(firefox_profile = firefox_profile)
browser.get("https://satconnect.intelsat.com/login")
browser.maximize_window()

time.sleep(5)

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
username.send_keys("username")
password.send_keys("password")

login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()

time.sleep(5)

browser.get("https://satconnect.intelsat.com/monitoring/report-generator")
time.sleep(5)

browser.find_elements_by_class_name("ui-tree-toggler").click()
time.sleep(5)
browser.find_elements_by_class_name('ui-chkbox-icon')[0].click()
time.sleep(5)
quit()