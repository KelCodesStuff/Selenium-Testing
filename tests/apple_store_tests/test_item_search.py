#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Import Chrome Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestAppleStoreSearch:
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
        self.browser.get("https://www.apple.com/")

        yield

        self.browser.quit()
        """Fixture to set up and teardown browser with optional headless and Selenoid mode"""

    def navigate_to_store(self):
        """Helper function to navigate to the Apple Store page"""
        try:
            store_menu = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Store"))
            )
            store_menu.click()
            assert "Store" in self.browser.title
        except TimeoutException:
            pytest.fail("Failed to navigate to Apple Store")

    def test_macbook_pro_search(self):
        """This test searches for a MacBook Pro and verifies results are displayed"""
        try:
            search_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.ac-gn-link-search"))
            )
            search_button.click()

            search_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "ac-gn-searchform-input"))
            )
            search_input.send_keys("MacBook Pro")
            search_input.submit()

            # Wait for results and verify at least one result is displayed
            results = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".as-explore-searchresults"))
            )

            assert "MacBook Pro" in self.browser.page_source
        except TimeoutException:
            pytest.fail("Search bar or search results not found or took too long")

    def test_ipad_pro_search(self):
        """This test searches for an iPad Pro and verifies results are displayed"""
        try:
            search_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.ac-gn-link-search"))
            )
            search_button.click()

            search_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "ac-gn-searchform-input"))
            )
            search_input.send_keys("iPad Pro")
            search_input.submit()

            # Wait for results and verify at least one result is displayed
            results = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".as-explore-searchresults"))
            )

            assert "MacBook Pro" in self.browser.page_source
        except TimeoutException:
            pytest.fail("Search bar or search results not found or took too long")

    def test_iphone_pro_search(self):
        """This test searches for an iPhone Pro Max and verifies results are displayed"""
        try:
            search_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.ac-gn-link-search"))
            )
            search_button.click()

            search_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "ac-gn-searchform-input"))
            )
            search_input.send_keys("iPhone Pro Max 16")
            search_input.submit()

            # Wait for results and verify at least one result is displayed
            results = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".as-explore-searchresults"))
            )

            assert "MacBook Pro" in self.browser.page_source
        except TimeoutException:
            pytest.fail("Search bar or search results not found or took too long")

    def test_invalid_search(self):
        """This test verifies an invalid search returns a 'no results' message"""
        try:
            search_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.ac-gn-link-search"))
            )
            search_button.click()

            search_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "ac-gn-searchform-input"))
            )
            search_input.send_keys("Non Existent Item 123")
            search_input.submit()

            # Wait for the "no results" message
            no_results_message = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".as-explore-noresults"))
            )

            assert "No results" in no_results_message.text
        except TimeoutException:
            pytest.fail("Search bar or no results message not found or took too long")

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