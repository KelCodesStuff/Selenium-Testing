#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Import Chrome Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestPlayStationStoreNavigation:
    # 1. Check browser configuration in browser_setup_and_teardown
    # 2. Run 'Selenium Tests' configuration
    # 3. Test report will be created in reports/ directory

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self, headless=True):
        """Fixture to set up and teardown browser with optional headless mode"""
        self.use_selenoid = False  # set to True to run tests with Selenoid

        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")  # Enable headless mode
            chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
            chrome_options.add_argument("--window-size=1920x1080")  # Set window size for headless mode

        if self.use_selenoid:
            self.browser = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub'
            )
        else:
            self.browser = webdriver.Chrome(options=chrome_options)  # Pass options here

        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get("https://www.apple.com/")

        yield

        self.browser.close()
        self.browser.quit()

    def test_store_navigation(self):
        """This test navigates to the Store page and verifies the page loaded"""
        try:
            store_menu = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Store"))
            )
            store_menu.click()

            # Verify that the Store page loaded
            assert "Store" in self.browser.title
        except TimeoutException:
            pytest.fail("Store menu item not found or click failed")

    def test_mac_menu(self):
        """This test checks presence of Mac menu item and clicks it"""
        try:
            mac_menu = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Mac"))
            )
            mac_menu.click()

            # Verify that the Mac page loaded
            assert "Mac" in self.browser.title
        except TimeoutException:
            pytest.fail("Mac menu item not found or click failed")

    def test_ipad_menu(self):
        """This test checks presence of iPhone menu item and clicks it"""
        try:
            iphone_menu = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "iPad"))
            )
            iphone_menu.click()

            # Verify that the iPhone page loaded
            assert "iPad" in self.browser.title
        except TimeoutException:
            pytest.fail("iPad menu item not found or click failed")

    def test_iphone_menu(self):
        """This test checks presence of iPhone menu item and clicks it"""
        try:
            iphone_menu = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "iPhone"))
            )
            iphone_menu.click()

            # Verify that the iPhone page loaded
            assert "iPhone" in self.browser.title
        except TimeoutException:
            pytest.fail("iPhone menu item not found or click failed")

'''
    def test_search_function(self):
        """this test checks search functionality on the Apple website"""
        # Use the 'id' attribute to locate the search button
        search_button = self.browser.find_element(By.ID, "globalnav-menubutton-link-search")
        search_button.click()

        # Locate the search field and enter the search term
        search_field = self.browser.find_element(By.CSS_SELECTOR, "input[type='search']")
        search_field.send_keys("iPhone 16")

        # Locate and click the submit button
        submit_button = self.browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # Verify that the search results page is displayed
        assert "iPhone 15" in self.browser.title or "Search" in self.browser.title
'''
