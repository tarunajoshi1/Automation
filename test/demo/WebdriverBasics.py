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
username = driver.find_element_by_xpath('''//*[@id="dnn_ctr9883_Login_Login_Membership_txtUsername"]''')
password = driver.find_element_by_xpath('''//*[@id="dnn_ctr9883_Login_Login_Membership_txtPassword"]''')
submit = driver.find_element_by_xpath('''//*[@id="dnn_ctr9883_Login_Login_Membership_cmdLogin"]''')


username.send_keys("anwoolford")
password.send_keys("TestUser123456")

submit.click()
# time delay to locate an element
time.sleep(10)
# click on post menu
driver.find_element_by_xpath('''//*[text()="Post"]''').click()
# click on add-post sub menu
driver.find_element_by_xpath('''//*[text()="Add Post"]''').click()

driver.find_element_by_xpath('''//input[@id='txtTitle']''').send_keys("Test by taruna")

# switching to iframe
driver.switch_to.frame('txtDescription_ifr')
driver.find_element_by_xpath('''//body[@id='tinymce']''').send_keys("Test by taruna")


actionChains = ActionChains(driver)
option = driver.find_element_by_class_name("mCSB_dragger_bar")
actionChains.click_and_hold(option).move_by_offset(0, 5000).release().perform()


A = driver.find_element_by_id("ddlPreviewType")
A.selectbyIndex(1)
