import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo= 2000)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
