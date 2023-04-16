import os

from selenium import webdriver
import pytest
from conftest import browser

def test_hello_worls(browser):
        
    browser.get('https://google.com')
    assert "Google" in browser.title

