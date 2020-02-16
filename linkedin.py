from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import threading
import time
import vars 

pr = webdriver.FirefoxProfile("/home/roz3x/.mozilla/firefox/xk1uxyq9.Parrot")
driver = webdriver.Firefox(pr)
# driver.maximize_window()
driver.implicitly_wait(5)

def linkedin():
    driver.get("https://www.linkedin.com")


    #finding the search button 
    elem = driver.find_element_by_xpath("//input[@class='search-global-typeahead__input always-show-placeholder']")
    elem.send_keys("distributed systems")
    elem.send_keys(Keys.RETURN) 
    # elem = driver.find_elements_by_xpath("//h3[@class='search-result__title t-16 t-black t-bold']")
    time.sleep(5)
    # elem = driver.find_element_by_xpath("//ul[contains(class,'search-results__list')]")
    elem = driver.execute_script('return document.getElementsByClassName("EntityPhoto-square-4 lazy-image loaded ember-view")')
    total_length = len(elem)
    print(total_length) # total jobs
    for i in range(total_length):
        time.sleep(3)
        el = driver.execute_script('return document.getElementsByClassName("EntityPhoto-square-4 lazy-image loaded ember-view")')
        el[i].click()
        time.sleep(4)
        try:
            apply_el = driver.execute_script('return document.getElementsByClassName("jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view")')
            apply_el.click()
            time.sleep(3)
        except:
            pass
        # going back 
        driver.execute_script("window.history.go(-1)")
    # for i in elem:
    #     # print(i)
    #     i.click()
    #     time.sleep(4)
    #     try:
    #         i = driver.execute_script('return document.getElementsByClassName("jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view")')
    #         i.click()
    #         time.sleep(3)
    #     except:
    #         pass
    #     driver.execute_script("window.history.go(-1)")


if __name__ == "__main__":
    linkedin()
