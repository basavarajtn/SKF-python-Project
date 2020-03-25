import time
from telnetlib import EC

from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

def test_skf():
    driver=Chrome(executable_path="C:\\Users\\basnitta\\PycharmProjects\\pytestFramework\\drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.skfbearingselect.com/")
    time.sleep(10)
    #driver.implicitly_wait(30)
    if driver.current_url=="https://www.skfbearingselect.com/#/privacy-notification":
        driver.find_element_by_xpath("//button[text()='Accept & continue']").click()

    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//img[@class='single-bearing']").click()
    driver.implicitly_wait(100)
#    driver.find_element_by_xpath("//span[text()='Select bearing type'']").click()
    #create object of the select
    driver.find_element_by_xpath("//span[text()='Select bearing type']").click()
    time.sleep(5)
    #ber=driver.find_element_by_xpath("//mat-option[contains(@id,'mat-option')]").text
    ber=driver.find_elements_by_xpath("//mat-option[contains(@id,'mat-option')]")
    count=0
    for skfber in ber:
        print(skfber.text)
        if skfber.text== "Insert bearing (Y-bearing)":
            print("Insert bearing (Y-bearing) is present in bearing list")
            count +=1
            exit()
    if count>len(ber):
        print("not present")
    print(count)


test_skf()