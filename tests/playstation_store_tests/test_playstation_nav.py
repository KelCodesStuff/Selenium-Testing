#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Import Chrome Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestPlaystationStoreNavigation:
    # 1. Check browser configuration in browser_setup_and_teardown
    # 2. Run 'Selenium Tests' configuration
    # 3. Test report will be created in reports/ directory

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self, headless=True, use_selenoid=False):
        """Fixture to set up and teardown browser with optional headless and Selenoid mode"""

        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920x1080")

        # Using Selenoid with Remote WebDriver
        if use_selenoid:
            # Set capabilities via chrome_options
            chrome_options.set_capability("browserName", "chrome")
            chrome_options.set_capability("version", "latest")
            chrome_options.set_capability("enableVNC", True)  # Optional, for UI access
            chrome_options.set_capability("enableVideo", True)  # Optional, for recording sessions

            # Using Selenoid with Remote WebDriver
            self.browser = webdriver.Remote(
                command_executor='http://localhost:4444/wd/hub',  # Selenoid Hub URL
                options=chrome_options
            )
        else:
            # Using local Chrome browser
            self.browser = webdriver.Chrome(options=chrome_options)  # Pass options here

        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get("https://direct.playstation.com/en-us")

        yield

        self.browser.quit()
        """Fixture to set up and teardown browser with optional headless and Selenoid mode"""

    def test_store_navigation(self):
        """This test navigates to the PlayStation Direct Store page and verifies the page loaded"""
        try:
            store_menu = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Explore PlayStation"))
            )
            store_menu.click()

            # Verify that the Store page loaded
            assert "Store" in self.browser.title
        except TimeoutException:
            pytest.fail("Store menu item not found or click failed")

    def test_ps5_consoles_menu(self):
        """This test checks presence of the PS5 Consoles menu button and clicks it"""
        try:
            mac_menu = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "PS5 Consoles"))
            )
            mac_menu.click()

            # Verify that the Mac page loaded
            assert "Mac" in self.browser.title
        except TimeoutException:
            pytest.fail("Mac menu item not found or click failed")

    def test_ps5_accessories_menu(self):
        """This test checks presence of PS5 Accessories menu button and clicks it"""
        try:
            iphone_menu = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "PS5 Accessories"))
            )
            iphone_menu.click()

            # Verify that the iPhone page loaded
            assert "iPad" in self.browser.title
        except TimeoutException:
            pytest.fail("iPad menu item not found or click failed")

    def test_games_menu(self):
        """This test checks presence of Games menu button and clicks it"""
        try:
            iphone_menu = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Games"))
            )
            iphone_menu.click()

            # Verify that the iPhone page loaded
            assert "iPhone" in self.browser.title
        except TimeoutException:
            pytest.fail("iPhone menu item not found or click failed")


