from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import unittest
import aos_methods as methods
import aos_locators as locators

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

class AosTestCases(unittest.TestCase):
    driver = webdriver.Chrome(options=options)

    @classmethod
    def setUpClass(cls):
        methods.set_up(cls.driver)

    @classmethod
    def test_1_create_new_user_validate_log_out(cls):
        methods.create_new_user(cls.driver)
        methods.validate_if_new_user_is_created(new_username=locators.username, driver=cls.driver)
        methods.log_out(username=locators.username, driver=cls.driver)

    @classmethod
    def test_2_log_in_and_validate(cls):
        methods.log_in(new_username=locators.username, new_password=locators.password, driver=cls.driver)
        methods.validate_if_new_user_can_log_in(new_username=locators.username, driver=cls.driver)

    @classmethod
    def test_4_checkout_shopping_cart(cls):
        methods.checkout_shopping_cart(username=locators.username, password=locators.password,
                                       full_name=locators.full_name,
                                       phone_number=locators.phone, driver=cls.driver)

    @classmethod
    def test_3_user_menu_validation(cls):
        methods.user_menu_validation(full_name=locators.full_name, username=locators.username, driver=cls.driver)

    @classmethod
    def test_5_delete_account(cls):
        methods.delete_user(username=locators.username, password=locators.password, full_name=locators.full_name,
                            driver=cls.driver)

    @classmethod
    def test_6_check_top_heading_menu_links_on_homepage_and_contact_us_form(cls):
        methods.check_top_heading_menu_links_on_homepage(driver=cls.driver)

    @classmethod
    def test_7_links_on_homepage_and_contact_us_form(cls):
        methods.check_all_texts_are_displayed_and_links_are_clickable_on_homepage(driver=cls.driver)

    @classmethod
    def test_8_check_contact_us_form(cls):
        methods.check_contact_us_form(driver=cls.driver, email=locators.email)

    @classmethod
    def tearDownClass(cls):
        methods.tear_down(cls.driver)
