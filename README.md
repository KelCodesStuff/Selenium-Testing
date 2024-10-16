# Selenium Testing Project

This project provides a robust automation testing framework using Selenium and PyTest to perform end-to-end testing. It focuses on testing various aspects of the websites, including the checkout process, performance, and load testing. The tests are configured to run on both **Chrome** and **Firefox** browsers. Aqua IDE is used for development.

## Key Features
- Automated Testing: Perform seamless navigation and testing of the Apple website, including automating the process of clicking the Buy button for a MacBook Pro.
- PyTest Framework: Efficient and scalable test structure utilizing fixtures for browser setup.
- Continuous Integration: Integrated with CircleCI for automated testing workflows.
- Performance and Load Testing: Automated performance and load testing with Locust.
- Custom Fixtures: Reusable test setup and teardown using Selenium WebDriver fixtures.
- Cross-Browser Testing: Expandable for testing on multiple browsers.

## Technologies

### Selenium
[Selenium](https://www.selenium.dev/) is a popular browser automation framework used to automate web applications for testing purposes. It supports multiple browsers and programming languages.

### PyTest
[PyTest](https://pytest.org/) is a powerful testing framework for Python. In this project, we use PyTest to manage and run the Selenium test cases.

### Selenoid
[Selenoid](https://aerokube.com/selenoid/) is a lightweight alternative to Selenium Grid, allowing browsers to run inside Docker containers. This project uses Selenoid to run tests in both Chrome and Firefox within Docker.

### Aqua IDE
[Aqua](https://aqua.cloud/) is an IDE designed specifically for test automation. This project uses Aqua IDE to develop and run Selenium tests.

## Setup

### Prerequisites

1. **Python 3.x** installed on your system.
2. **Docker** installed and running for Selenoid.
3. **Aqua IDE** for development.
4. **Chrome and Firefox** installed on your system for local testing.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KelCodesStuff/Selenium-Testing.git
   cd selenium-testing
