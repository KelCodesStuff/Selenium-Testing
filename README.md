# Selenium Testing Project

This project contains automated tests for navigating and interacting with websites using Selenium, PyTest, and Selenoid for browser automation. The tests are configured to run on both **Chrome** and **Firefox** browsers. Aqua IDE is used for development.

## Table of Contents
- [Technologies](#technologies)
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Headless Mode](#headless-mode)
- [Selenoid Configuration](#selenoid-configuration)
- [Aqua IDE](#aqua-ide)

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
   git clone https://github.com/your-repo/selenium-testing.git
   cd selenium-testing
