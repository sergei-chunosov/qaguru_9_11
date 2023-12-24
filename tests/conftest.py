import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_settings_demoqa():
    browser.config.base_url = "https://demoqa.com/"
    browser.config.window_width = '1900'
    browser.config.window_height = '1080'
    browser.config.timeout = 4
