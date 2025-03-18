from pages.base_page import BasePage


class ApplyPage(BasePage):
    """Apply page object for the Y Combinator website"""

    def __init__(self, page):
        """Initialize the ApplyPage with selectors"""
        super().__init__(page)

        # Selectors based on the Apply page HTML
        self.apply_now_button = ".ycdc-btn"  # The "Apply to Spring 2025" button
        self.page_title = ".ycdc-page-title"
        self.apply_heading = "h1:text('Apply to Y Combinator')"
        self.batch_info = ".ycdc-page-updated"  # Contains batch information

    def is_apply_now_button_visible(self):
        """Check if the Apply Now button is visible on the page"""
        return self.is_element_visible(self.apply_now_button)

    def get_page_title(self):
        """Get the title of the current page"""
        return self.get_element_text(self.page_title)

    def is_on_apply_page(self):
        """Check if we're on the apply page"""
        # Check for multiple indications that we're on the Apply page
        url_check = "/apply" in self.page.url
        heading_check = self.is_element_visible(self.apply_heading)
        button_check = self.is_apply_now_button_visible()

        # Need at least the URL and one other check to pass
        return url_check and (heading_check or button_check)
