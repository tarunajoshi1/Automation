from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from   selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time, imaplib

driver = webdriver.Chrome("C:\\Users\\taruna.joshi.KELLTONGGN\\PycharmProjects\\demopython\\Drivers\\chromedriver.exe")
driver.get("http://rt19test.parasense.com/record-event")
driver.maximize_window()
# passing login id and password to click on login button
username = driver.find_element_by_xpath('''//input[@formcontrolname="username"]''')
password = driver.find_element_by_xpath('''//input[@formcontrolname="password"]''')
submit = driver.find_element_by_xpath('''//button[contains(text(), 'Login')]''')


username.send_keys("jaipal.singh@kelltontech.com")
password.send_keys("jaipal")

submit.click()

driver.implicitly_wait(5)
##driver.find_element_by_xpath("//input[@class='form-control ng-valid ng-touched ng-dirty']").send_keys("Giant Eagle").click()
driver.find_element_by_xpath("//li[contains(.,'Giant')]").click()
driver.find_element_by_xpath("//li[@class='regionElement'][2]").click()
time.sleep(3)
driver.find_element_by_xpath("//ul//li[contains(text(),'Am')]").click()
#//ul//li[contains(text(),'Am')]
driver.find_element_by_xpath("//li[@class= 'applianceElement glyphicon glyphicon-ok'][1]").click()