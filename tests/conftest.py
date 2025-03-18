import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Define default browser context arguments"""
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
    }


@pytest.fixture(scope="session")
def browser(playwright, browser_type):
    """Create a browser instance for testing"""
    print(f"\nBrowser type selected: {browser_type}")  # Debug print
    if browser_type.name == "webkit":
        print("Launching WebKit")
        browser = playwright.webkit.launch(headless=False)
    elif browser_type.name == "firefox":
        print("Launching Firefox")
        browser = playwright.firefox.launch(headless=False)
    else:
        print("Launching Chromium")
        browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    """Create a new page for each test"""
    page = browser.new_page()
    yield page
    page.close()
