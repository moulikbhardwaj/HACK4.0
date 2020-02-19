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

def linkedin():
    driver.get("https://www.linkedin.com")

    #finding the search button 
    elem = driver.find_element_by_xpath("//input[@class='search-global-typeahead__input always-show-placeholder']")
    elem.send_keys(".net")
    elem.send_keys(Keys.RETURN) 
    # elem = driver.find_elements_by_xpath("//h3[@class='search-result__title t-16 t-black t-bold']")
    time.sleep(3)

    driver.find_element_by_xpath("//span[@class='artdeco-button__text' and text()='LinkedIn Features']").click()
    driver.find_element_by_xpath("//span[@class='search-s-facet-value__name t-14 t-black--light t-normal' and text() = 'Easy Apply']").click()
    driver.find_elements_by_xpath("//button[@class='facet-collection-list__apply-button ml2 artdeco-button artdeco-button--2 artdeco-button--primary ember-view' and @data-control-name = 'filter_pill_apply']")[0].click()
    test = driver.find_element_by_xpath("//ul[@class='jobs-search-results__list artdeco-list']")
    test = test.find_elements_by_xpath('//li[@class="occludable-update artdeco-list__item--offset-4 artdeco-list__item p0 ember-view"]')
    n = len(test)
    for i in range(n):
        test = driver.find_element_by_xpath("//ul[@class='jobs-search-results__list artdeco-list']")
        test = test.find_elements_by_xpath('//li[@class="occludable-update artdeco-list__item--offset-4 artdeco-list__item p0 ember-view"]')
        test[i].click()
        time.sleep(4)
        try:
            driver.find_element_by_xpath("//button[@class='jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view']").click()
            try:
                driver.find_element_by_xpath('//span[@class="artdeco-button__text" and text() = "Submit application"]').click()
                try:
                    driver.find_element_by_xpath("//span[@class='artdeco-button__text' and text() = 'Not now']").click()
                except:
                    pass
                time.sleep(1)
                
            except:
                driver.find_element_by_xpath("//button[@class='artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view']").click()
                driver.find_element_by_xpath("//span[@class='artdeco-button__text' and text() = 'Discard']").click()
                
                pass
            # try:

            #     test = driver.find_element_by_xpath("//div[@class='jobs-easy-apply-form-section__grouping']")
            #     # test = test.find_element_by_xpath("//span[@role = 'Upload resume']")
            #     # apply_el = driver.execute_script('return document.getElementsByClassName("jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view")')
            #     # apply_el[0].click()
            # except:
            #     pass
        except:
            pass
        # driver.execute_script("window.history.go(-1)")

if __name__ == "__main__":
    linkedin()
