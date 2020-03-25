from selenium.webdriver import Chrome
import time

def before_all(context):
    context.driver=Chrome(executable_path="C:\\Users\\basnitta\\PycharmProjects\\pytestFramework\\drivers\\chromedriver.exe")
    context.driver.maximize_window()
    context.driver.get("https://www.skfbearingselect.com/")
    time.sleep(5)

    if context.driver.current_url=="https://www.skfbearingselect.com/#/privacy-notification":
        context.driver.find_element_by_xpath("//button[text()='Accept & continue']").click()
    context.driver.implicitly_wait(30)

    if context.driver.current_url=="https://www.skfbearingselect.com/#/privacy-notification":
        context.driver.find_element_by_xpath("//button[text()='Accept & continue']").click()

    context.driver.implicitly_wait(30)
    context.driver.find_element_by_xpath("//img[@class='single-bearing']").click()
    context.driver.implicitly_wait(100)
    context.driver.find_element_by_xpath("//span[text()='Select bearing type']").click()
    time.sleep(5)

def after_all(context):
    context.driver.close()

