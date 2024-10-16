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

    def test_ps5_search(self):
        """This test searches for a PlayStation 5 and verifies results are displayed"""
        try:
            search_box = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))  # Adjust if search bar has a different name
            )
            search_box.send_keys("PS5 Console")
            search_box.submit()

            # Verify search results page loaded
            results_text = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".search-results"))
            )
            assert "PS5 Console" in results_text.text
        except TimeoutException:
            pytest.fail("Search box or results not found or search failed")

    def test_portal_search(self):
        """This test searches for a PlayStation Portal and verifies results are displayed"""
        try:
            search_box = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))  # Adjust if search bar has a different name
            )
            search_box.send_keys("PlayStation Portal")
            search_box.submit()

            # Verify search results page loaded
            results_text = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".search-results"))
            )
            assert "PS5 Console" in results_text.text
        except TimeoutException:
            pytest.fail("Search box or results not found or search failed")

    def test_dualsense_search(self):
        """This test searches for a DualSense and verifies results are displayed"""
        try:
            search_box = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))  # Adjust if search bar has a different name
            )
            search_box.send_keys("PlayStation Portal")
            search_box.submit()

            # Verify search results page loaded
            results_text = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".search-results"))
            )
            assert "PS5 Console" in results_text.text
        except TimeoutException:
            pytest.fail("Search box or results not found or search failed")

    def test_search_invalid_item(self):
        """This test searches for an invalid or non-existent item and verifies error handling"""
        try:
            search_box = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))  # Adjust if search bar has a different name
            )
            search_box.send_keys("InvalidSearchTerm123")
            search_box.submit()

            # Verify error message or no results page
            no_results_text = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".no-results"))
            )
            assert "No results found" in no_results_text.text
        except TimeoutException:
            pytest.fail("Search box or no results message not found")

    def test_search_empty_input(self):
        """This test submits an empty search query and checks how the page handles it"""
        try:
            search_box = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))  # Adjust if search bar has a different name
            )
            search_box.send_keys("")  # Empty input
            search_box.submit()

            # Check for any validation or error message
            error_message = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message"))
            )
            assert "Please enter a search term" in error_message.text
        except TimeoutException:
            pytest.fail("Search box or error message not found")

