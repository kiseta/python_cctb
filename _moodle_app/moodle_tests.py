import unittest

import moodle_locators as locators
import moodle_methods as methods


class MoodleAppPositiveTestCases(unittest.TestCase): # create class

    @staticmethod # signal to UnitTest that this is a static method (function inside class) vs classmethod
    def test_create_new_user(): # test_ in the name is mandatory
        methods.setUp()
        methods.log_in(locators.moodle_username, locators.moodle_password)
        methods.create_new_user()
        methods.search_user()
        methods.log_out()
        methods.log_in(locators.new_username, locators.new_password)
        methods.check_new_user_can_login()
        methods.log_out()
        methods.log_in(locators.moodle_username, locators.moodle_password)
        methods.delete_user()
        methods.log_out()
        methods.tearDown()


    @staticmethod # signal to UnitTest that this is a static method (function inside class) vs classmethod
    def test_create_new_user_min():
        methods.setUp()
        methods.log_in(locators.moodle_username, locators.moodle_password)
        methods.create_new_user()
        methods.delete_user()
        methods.log_out()
        methods.tearDown()
