from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import re
import threading
import pickle
import time
import vars

pr = webdriver.FirefoxProfile("/home/moulik/.mozilla/firefox/co19xs3p.default-release")
driver = webdriver.Firefox(pr)
driver.maximize_window()
driver.implicitly_wait(1)

def main():

    driver.get("https://www.indeed.co.in")
    assert "Indeed" in driver.title

    #check not logged in
    try:
        # time.sleep(2)
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
    time.sleep(2)
    elem = driver.find_element_by_id("text-input-what")
    elem.send_keys("Frontend Developer")
    elem = driver.find_element_by_id("text-input-where")
    elem.clear()
    elem.send_keys(Keys.RETURN)
    try:
        time.sleep(2)
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
    time.sleep(2)
    elem = driver.find_elements_by_xpath("//div[@class='jobsearch-SerpJobCard unifiedRow row result clickcard']//span[@class='iaLabel iaIconActive']")
            
    for i in elem[4:]:
        #card selection
        i.click()
        
        #apply now
        try:
            time.sleep(2)
            el = driver.find_element_by_xpath("//span[@class='indeed-apply-widget indeed-apply-button-container js-IndeedApplyWidget indeed-apply-status-not-applied']")
        except:
            el = driver.find_element_by_xpath("//span[@class='indeed-apply-button-label']")
        el.click()
        time.sleep(2)

        #iframe switch
        time.sleep(2)
        el = driver.find_element_by_xpath("//iframe[contains(@name, 'indeed-ia')]")        
        driver.switch_to.frame(el)
        el = driver.find_element_by_xpath("//iframe[@title='Apply Now']")        
        driver.switch_to.frame(el)
        time.sleep(5)
        #phone number
        # el = driver.find_element_by_xpath('//input[@id="input-applicant.phoneNumber"]')
        # el.clear()
        # el.send_keys(vars.phone)

        #add cover letter
        try:
            el = driver.find_element_by_xpath('//button[@class="icl-Button icl-Button--transparent icl-Button--sm ia-AddCoverLetter-button"]')
            el.click()
        except:
            pass
        try:
            el = driver.find_element_by_xpath("//textarea[@id='textarea-applicant.applicationMessage']")
            el.clear()
            el.send_keys(vars.cover_letter)
        except:
            pass

        #whatsapp false
        try:
            el = driver.find_element_by_xpath("//input[@id='smsOptIn']")
            if(el.is_selected()):
                el.click()
        except:
            pass

        #email_me true
        try:
            el = driver.find_element_by_xpath("//input[@id='makeJobAlert']")
            if el.is_selected()==False:
                el.click()
        except:
            pass

        #click continue
        el = driver.find_element_by_xpath("//button[@id='form-action-continue']")
        time.sleep(1)
        el.click()

        #regex here
        el = driver.find_elements_by_xpath("//div[@class='ia-ScreenerQuestions']")
        n = len(el)
        print(n)
        for i in range(n):
            print(i)
            el = driver.find_element_by_xpath("//div[@class='ia-ScreenerQuestions']/parent::div[@class!='icl-u-visuallyHidden']")
            time.sleep(1)
            question_solver(el)
            driver.find_element_by_xpath("//button[@id='form-action-continue']").click()
        time.sleep(5)
        ele = driver.find_element_by_xpath("//button[@id='form-action-submit']")
        action = ActionChains(driver)
        action.move_to_element(ele).click().perform()
        # ele.click()
        time.sleep(5)
        try:
            while len(driver.find_elements_by_xpath("//a[@id='form-action-back']"))>0:
                ele = driver.find_element_by_xpath("//a[@id='form-action-back']")
                ele.click()
            ele = driver.find_element_by_xpath("//a[@id='form-action-cancel']")
            ele.click()
        except:
            pass;            
        driver.switch_to.default_content()            

def popChk():
    while True:
        try:
            el = driver.find_element_by_id("popover-close-link")
            el.click()
            break
        except:
            pass

def question_solver(elem):
    indivs = elem.find_elements_by_xpath(".//div/child::div[@class='icl-TextInput']")
    for question in indivs:
        #regex required for text
        text = question.find_element_by_tag_name("span").get_attribute('textContent').lower()
        my_re = re.compile(r"of (.*) experience")
        ip = question.find_element_by_xpath(".//input[@class='icl-TextInput-control icl-TextInput-control--sm']")
        print(text)
        flag = 1
        for key in vars.exp:
            if text.find(key.lower())!=-1:
                print(key, vars.exp[key])
                ip.clear()
                ip.send_keys(vars.exp[key])
                flag = 0
                break
        if(flag==1):
            ip.send_keys(0)
        # question.send_keys(Keys.RETURN)

if __name__ == "__main__":
    main()
