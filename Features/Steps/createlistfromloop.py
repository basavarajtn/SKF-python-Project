from behave import *
from selenium.webdriver import Chrome
from hamcrest import assert_that
from hamcrest.library.collection.issequence_containinginanyorder import contains_inanyorder
import time


@then(u'All the below listed option should be visable')
def step_impl(context):
    expected_result = [row["BearingList"] for row in context.table]
    opts_list = context.driver.find_elements_by_xpath("//mat-option[contains(@id,'mat-option')]")
    actual_result = [opt.text for opt in opts_list]
    assert_that(expected_result, contains_inanyorder(*actual_result))
