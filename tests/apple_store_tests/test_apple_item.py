#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Import Chrome Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestAppleStoreItem:
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

    def test_macbook_pro_description(self):
        """Test to verify product description"""
        self.navigate_to_store()

        # Directly navigate to the product page (Shop Mac)
        self.browser.get("https://www.apple.com/shop/buy-mac")

        # Wait for the page to load and locate the 'Buy' button for the MacBook Pro
        buy_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-autom='MBP_M3_MAIN']")),
            message="Buy button for MacBook Pro not found"
        )
        buy_button.click()

        # Locate the 'M3 Max' button for the MacBook Pro
        model_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "tab-:rb:-3")),
            message="Model button for M3 Max not found"
        )
        model_button.click()

        # Verify the item description
        item_description = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "productbundle-title-14inch-supreme")),
            message="Item description for MacBook Pro M3 Max not found"
        )

        # Verify the description text matches expected value
        assert "MacBook Pro M3 Max" in item_description.text, "The MacBook Pro M3 Max description does not match"


    def test_ipad_pro_description(self):
        """Test to verify product description"""
        self.navigate_to_store()

        # Directly navigate to the product page (Shop Mac)
        self.browser.get("https://www.apple.com/shop/buy-mac")

        # Wait for the page to load and locate the 'Buy' button for the MacBook Pro
        buy_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-autom='MBP_M3_MAIN']")),
            message="Buy button for MacBook Pro not found"
        )
        buy_button.click()

        # Locate the 'M3 Max' button for the MacBook Pro
        model_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "tab-:rb:-3")),
            message="Model button for M3 Max not found"
        )
        model_button.click()

        # Verify the item description
        item_description = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "productbundle-title-14inch-supreme")),
            message="Item description for MacBook Pro M3 Max not found"
        )

        # Verify the description text matches expected value
        assert "MacBook Pro M3 Max" in item_description.text, "The MacBook Pro M3 Max description does not match"

    def test_iphone_pro_description(self):
        """Test to verify product description"""
        self.navigate_to_store()

        # Directly navigate to the product page (Shop Mac)
        self.browser.get("https://www.apple.com/shop/buy-mac")

        # Wait for the page to load and locate the 'Buy' button for the MacBook Pro
        buy_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-autom='MBP_M3_MAIN']")),
            message="Buy button for MacBook Pro not found"
        )
        buy_button.click()

        # Locate the 'M3 Max' button for the MacBook Pro
        model_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.ID, "tab-:rb:-3")),
            message="Model button for M3 Max not found"
        )
        model_button.click()

        # Verify the item description
        item_description = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "productbundle-title-14inch-supreme")),
            message="Item description for MacBook Pro M3 Max not found"
        )

        # Verify the description text matches expected value
        assert "MacBook Pro M3 Max" in item_description.text, "The MacBook Pro M3 Max description does not match"