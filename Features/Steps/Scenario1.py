from behave import *
from selenium.webdriver import Chrome
from hamcrest import assert_that
from hamcrest.library.collection.issequence_containinginanyorder import contains_inanyorder
import time

@then(u'All the below listed option should be visable "{BearingList}"')
def step_impl(context,BearingList):
    ber=context.driver.find_elements_by_xpath("//mat-option[contains(@id,'mat-option')]")

    count=0
    for skfber in ber:
        if skfber.text==BearingList:
            print(BearingList + "   is present in bearing list")
            print(len(skfber.text))
            break
        count = count + 1
        if (count==14 and skfber.text!=BearingList):
                print(BearingList + "   not present")
                #assert skfber.text==BearingList

