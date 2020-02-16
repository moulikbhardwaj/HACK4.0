from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading
import pickle
import time
import vars

pr = webdriver.FirefoxProfile("/home/roz3x/.mozilla/firefox/xk1uxyq9.Parrot")
driver = webdriver.Firefox(pr)
driver.maximize_window()
driver.implicitly_wait(5)

def main():

    driver.get("https://www.indeed.co.in")
    assert "Indeed" in driver.title

    #check not logged in
    try:
        elem = driver.find_element_by_link_text("Sign in")
        elem.click()
        elem = driver.find_element_by_id("login-email-input")
        elem.send_keys(vars.email)
        elem = driver.find_element_by_id("login-password-input")
        elem.send_keys(vars.PASSWORD)
        elem.send_keys(Keys.RETURN)
    except:
        pass

    #search for backend intern
    elem = driver.find_element_by_id("text-input-what")
    elem.send_keys("Backend Developer")
    elem = driver.find_element_by_id("text-input-where")
    elem.clear()
    elem.send_keys(Keys.RETURN)
    try:
        elem = driver.find_element_by_xpath("//a[contains(@title, 'Internship') ]")
        elem.click()
    except:
        elem = driver.find_element_by_id("filter-job-type")
        elem.click()
        elem = driver.find_element_by_xpath("//a[contains(@title, 'Internship') ]")
        elem.click()
    
    #check for popups
    th = threading.Thread(target=popChk)
    th.start()

    #search for indeed resume applicable jobs
    elem = driver.find_elements_by_xpath("//div[@class='jobsearch-SerpJobCard unifiedRow row result clickcard']//span[@class='iaLabel iaIconActive']")
    for i in elem[:1]:
        #card selection
        i.click()
        
        #apply now
        el = driver.find_element_by_xpath("//span[@class='indeed-apply-widget indeed-apply-button-container js-IndeedApplyWidget indeed-apply-status-not-applied']")
        el.click()

        #iframe switch
        el = driver.find_element_by_xpath("//iframe[contains(@name, 'indeed-ia')]")        
        driver.switch_to.frame(el)
        el = driver.find_element_by_xpath("//iframe[@title='Apply Now']")        
        driver.switch_to.frame(el)

        #phone number
        el = driver.find_element_by_xpath('//input[@id="input-applicant.phoneNumber"]')
        el.clear()
        el.send_keys(vars.phone)

        #add cover letter
        el = driver.find_element_by_xpath('//button[@class="icl-Button icl-Button--transparent icl-Button--sm ia-AddCoverLetter-button"]')
        el.click()
        el = driver.find_element_by_xpath("//textarea[@id='textarea-applicant.applicationMessage']")
        el.clear()
        el.send_keys(vars.cover_letter)


def popChk():
    while True:
        try:
            el = driver.find_element_by_id("popover-close-link")
            el.click()
            break
        except:
            pass

if __name__ == "__main__":
    main()
