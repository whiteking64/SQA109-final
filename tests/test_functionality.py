from pages.apply_page import ApplyPage
from pages.home_page import HomePage


class TestFunctionality:
    """Tests for button functionality"""

    # Test Case 5: Verifying the 'Apply' Button Functionality
    def test_apply_button_functionality(self, page):
        """
        Test Case 5: Verifying the 'Apply' Button Functionality

        Steps:
        1. Navigate to the home page
        2. Click on the Apply button
        3. Verify navigation to the application page
        4. Verify that the expected content (Apply Now button) is loaded
        """
        # Arrange & Act
        home_page = HomePage(page)
        home_page.navigate_to_home()
        home_page.click_apply_button()

        # Assert - Create ApplyPage only when needed for assertions
        apply_page = ApplyPage(page)
        assert "apply" in page.url.lower(), "URL does not contain 'apply'"
        assert apply_page.is_apply_now_button_visible(), "Apply Now button is not visible"
        assert "Apply" in apply_page.get_page_title(), "Page title does not contain 'Apply'"
