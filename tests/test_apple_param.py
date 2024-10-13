#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Import Chrome Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestAppleWebsite:
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

    @pytest.mark.parametrize("menu_text, expected_title", [
        ("Store", "Store"),
        ("Mac", "Mac"),
        ("iPad", "iPad"),
        ("iPhone", "iPhone")
    ])
    def test_menu_navigation(self, menu_text, expected_title):
        """This test navigates to the given menu item and verifies the page loaded"""
        try:
            menu_item = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, menu_text))
            )
            menu_item.click()

            # Verify that the correct page loaded
            assert expected_title in self.browser.title
        except TimeoutException:
            pytest.fail(f"{menu_text} menu item not found or click failed")