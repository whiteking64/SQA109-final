from playwright.sync_api import TimeoutError


class BasePage:
    """Base page object with common methods for all pages"""

    def __init__(self, page):
        """Initialize the BasePage with a Playwright page object"""
        self.page = page
        self.base_url = "https://www.ycombinator.com"
        self.timeout = 30000  # 30 seconds default timeout

    def navigate_to(self, path=""):
        """Navigate to a specific path from the base URL"""
        full_url = f"{self.base_url}/{path}"
        self.page.goto(full_url)
        try:
            self.page.wait_for_load_state("networkidle", timeout=self.timeout)
        except TimeoutError as e:
            raise TimeoutError(f"Page load timeout for {full_url}") from e

    def get_element_text(self, selector):
        """Get the text content of an element"""
        return self.page.text_content(selector)

    def click_element(self, selector):
        """Click on an element"""
        self.page.click(selector)
        self.page.wait_for_load_state("networkidle")

    def is_element_visible(self, selector, timeout=5000):
        """Check if an element is visible on the page"""
        return self.page.is_visible(selector, timeout=timeout)

    def wait_for_element(self, selector, timeout=None):
        """Wait for an element to be visible"""
        try:
            return self.page.wait_for_selector(selector, state="visible", timeout=timeout or self.timeout)
        except TimeoutError as e:
            raise TimeoutError(f"Element not found: {selector}") from e

    def scroll_to_bottom(self):
        """Scroll to the bottom of the page"""
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        # Wait a bit for any dynamic content to load
        self.page.wait_for_timeout(1000)

    def scroll_to_element(self, selector):
        """Scroll to a specific element"""
        element = self.page.query_selector(selector)
        if element:
            element.scroll_into_view_if_needed()
            self.page.wait_for_timeout(500)
