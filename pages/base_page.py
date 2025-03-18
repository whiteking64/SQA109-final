class BasePage:
    """Base page object with common methods for all pages"""

    def __init__(self, page):
        """Initialize the BasePage with a Playwright page object"""
        self.page = page
        self.base_url = "https://www.ycombinator.com"

    def navigate_to(self, path=""):
        """Navigate to a specific path from the base URL"""
        full_url = f"{self.base_url}/{path}"
        self.page.goto(full_url)
        self.page.wait_for_load_state("networkidle")

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

    def wait_for_element(self, selector, timeout=10000):
        """Wait for an element to be visible"""
        return self.page.wait_for_selector(selector, state="visible", timeout=timeout)

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
