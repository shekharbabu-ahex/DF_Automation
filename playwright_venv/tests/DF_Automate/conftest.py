import pytest
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture(scope="function")
def page(browser):  # Use browser fixture
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


# @pytest.fixture(scope="function")
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         yield page
#         browser.close()