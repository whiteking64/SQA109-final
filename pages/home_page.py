from pages.base_page import BasePage


class HomePage(BasePage):
    """Home page object for the Y Combinator website"""

    def __init__(self, page):
        """Initialize the HomePage with selectors"""
        super().__init__(page)

        # Navigation elements with specific selectors based on actual HTML
        self.library_link = "a[href='/library']"
        # Use the very specific selector for the Apply button
        self.apply_button = "a.apply-btn.ycdc-retro-btn[href='/apply']"

    def navigate_to_home(self):
        """Navigate to the home page"""
        self.navigate_to("")

    def navigate_to_library(self):
        """Click on the Library link in the navigation"""
        self.click_element(self.library_link)

    def click_apply_button(self):
        """Click on the Apply button in the navigation"""
        # Make sure we wait for the button to be visible before clicking
        self.wait_for_element(self.apply_button)
        self.click_element(self.apply_button)
