from pages.base_page import BasePage


class LibraryPage(BasePage):
    """Library page object for the Y Combinator website"""

    def __init__(self, page):
        """Initialize the LibraryPage with selectors"""
        super().__init__(page)

        # Using a more specific XPath that follows the exact DOM structure
        self.latest_link = "//div[@class='mx-auto max-w-ycdc-page']/section[3]//div[@class='mb-2 decoration-2']/div[contains(text(), 'The Latest')]"
        self.page_title = "h1, .text-2xl.font-normal.text-neutral-600"

    def navigate_to_library(self):
        """Navigate directly to the library page"""
        self.navigate_to("library")
        # Wait for the page to fully load
        self.page.wait_for_load_state("networkidle")

    def navigate_to_latest(self):
        """Navigate to 'The Latest' page"""
        # First make sure we're on the library page
        if "library" not in self.page.url:
            self.navigate_to_library()

        # Try to find The Latest element
        latest_element = self.page.query_selector(self.latest_link)
        if latest_element:

            # Get the title attribute which contains the URL
            title_attr = latest_element.get_attribute("title")
            if title_attr and "https://" in title_attr:
                # Navigate directly to the URL from the title attribute
                self.page.goto(title_attr)
            else:
                raise ValueError("No URL found in title attribute")
        else:
            raise ValueError("'The Latest' element not found with current selector")

        self.page.wait_for_load_state("networkidle")

    def get_page_title(self):
        """Get the title of the current page"""
        return self.get_element_text(self.page_title)

    def is_on_library_page(self):
        """Check if we're on the library page"""
        return "library" in self.page.url
