#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Import Chrome Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestAppleStoreCheckout:
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
        """Helper function to navigate to the Store page"""
        try:
            store_menu = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Store"))
            )
            store_menu.click()
            assert "Store" in self.browser.title
        except TimeoutException:
            pytest.fail("Failed to navigate to Apple Store")

    def test_add_item_to_cart(self):
        """Test to add a product to the cart"""
        self.navigate_to_store()

        try:
            # Locate and click on a product (e.g., MacBook)
            product = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/macbook-air/']"))
            )
            product.click()

            # Add product to cart
            add_to_cart_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".add-to-cart-button"))
            )
            add_to_cart_button.click()

            # Verify that the product is added to the cart
            cart_icon = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-icon"))
            )
            cart_icon.click()

            # Verify cart has the item
            cart_item = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-product-title")),
                message="Item price element is not visible"
            ).text
            assert "MacBook Air" in cart_item, "Item not found in the cart"
        except TimeoutException:
            pytest.fail("Failed to add product to the cart")

    def test_item_checkout(self):
        """Test to navigate through the checkout process"""
        self.test_add_item_to_cart()

        try:
            # Proceed to checkout
            checkout_button = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-button"))
            )
            checkout_button.click()

            # Verify navigation to the checkout page
            assert "Checkout" in self.browser.title, "Failed to navigate to checkout"
        except TimeoutException:
            pytest.fail("Checkout navigation failed")