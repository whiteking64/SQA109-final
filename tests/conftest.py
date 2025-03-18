import pytest
from playwright.sync_api import sync_playwright


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
def browser():
    """Create a browser instance for testing"""
    playwright = sync_playwright().start()
    # Set headless=False to see the browser
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=50,  # Add 50ms delay between actions
        args=["--start-maximized"],  # Start with maximized window
    )
    yield browser
    browser.close()
    playwright.stop()


@pytest.fixture
def page(browser):
    """Create a new page for each test"""
    page = browser.new_page()
    yield page
    page.close()


# Fixture to run in non-headless mode
@pytest.fixture(scope="session")
def browser_launch_args(browser_launch_args):
    return {
        **browser_launch_args,
        "headless": False,
        "slow_mo": 100,  # Add a small delay between actions for better visibility
    }
