from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import threading
import time
import vars 

pr = webdriver.FirefoxProfile("/home/moulik/.mozilla/firefox/co19xs3p.default-release")
driver = webdriver.Firefox(pr)
# driver.maximize_window()
driver.implicitly_wait(5)

def gmail():
    driver.get('https://mail.google.com/mail/u/2')
    elem = driver.find_element_by_xpath("//input[@placeholder='Search mail']")
    elem.send_keys("Linkedin new jobs")
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
    # finding spans with only linkedin 
    elem = driver.find_elements_by_xpath("//span[text()='LinkedIn']")
    # list of all the linkedin's
    total_elems = len(elem)
    for i in range(total_elems):
        time.sleep(5)
        el = driver.find_elements_by_xpath("//span[text()='LinkedIn']")
        driver.execute_script("""arguments[0].click()""",el[i])
        time.sleep(5)
        
        # finding the job links 
        links = driver.find_elements_by_xpath("//a[contains(@href,'https://www.linkedin.com/comm/jobs/view/')]")
        # print(links)
        for t in range(len(links)):
            el = driver.find_elements_by_xpath("//a[contains(@href,'https://www.linkedin.com/comm/jobs/view/')]")
            driver.execute_script("""arguments[0].click()""",el[t])
            time.sleep(6)
            driver.execute_script("window.history.go(-1);")


        driver.execute_script("window.history.go(-1);")



if __name__ == '__main__':
    gmail()