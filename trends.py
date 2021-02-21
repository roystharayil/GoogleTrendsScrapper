'''
[01] To scrape Google Trends with keywords
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path="C:\\Users\\DELL\\Downloads\\geckodriver\\geckodriver.exe")


def trends(keyword):
    driver.get("https://trends.google.com/trends")

    elem = driver.find_element_by_xpath('//*[@id="input-254"]')
    elem.clear()
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    csvIcon = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]')

    csvIcon.click()
