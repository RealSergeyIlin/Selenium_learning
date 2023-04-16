import pytest
from selenium import webdriver
import os
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirfoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

ff_binary_path = r'C:\\Mozilla Firefox\\firefox.exe'

ff_driver_path = r'C:\\browserdrivers\\geckodriver.exe'
chrome_driver_path = r'C:\\browserdrivers\\chromedriver.exe'
yandex_driver_path = r'C:\\browserdrivers\\yandexdriver.exe'
edge_driver_path = r'C:\\browserdrivers\\msedgedriver.exe'

def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome"
    )
    parser.addoption(
        "--headless", action="store_true"
    )

@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = None

    if _browser == 'firefox' or _browser == 'ff':
        options = FirfoxOptions()
        options.binary_location = ff_binary_path
        options.headless = headless

        driver = webdriver.Firefox(executable_path=ff_driver_path, options=options)
    elif _browser == 'chrome':
        options = ChromeOptions()
        options.headless = headless

        driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
    elif _browser == 'yandex':
        options = ChromeOptions()
        options.headless = headless

        driver = webdriver.Chrome(executable_path=yandex_driver_path, options=options)
    elif _browser == 'edge':
        options = EdgeOptions()
        options.headless = headless

        driver = webdriver.Edge(executable_path=edge_driver_path, options=options)

    driver.maximize_window()
    yield driver

    driver.close()
