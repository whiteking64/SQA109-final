from pages.home_page import HomePage
from pages.library_page import LibraryPage


class TestNavigation:
    """Tests for navigation functionality"""

    # Test Case 1: Navigating to the Library Link
    def test_navigate_to_library(self, page):
        """
        Test Case 1: Navigating to the Library Link

        Steps:
        1. Navigate to the home page
        2. Click on the Library link
        3. Verify that we are on the Library page
        """
        # Arrange & Act
        home_page = HomePage(page)
        home_page.navigate_to_home()
        home_page.navigate_to_library()

        # Assert
        assert "library" in page.url, "URL does not contain 'library'"

    # Test Case 2: Navigating to 'The Latest' Section
    def test_navigate_to_latest(self, page):
        """
        Test Case 2: Navigating to 'The Latest' Section

        Steps:
        1. Navigate to the Library page
        2. Click on 'The Latest' link
        3. Verify that we are on 'The Latest' page
        """
        # Arrange
        library_page = LibraryPage(page)

        # Act
        library_page.navigate_to_library()
        library_page.navigate_to_latest()

        # Assert
        # Check if we've navigated to a page with "The Latest" in the URL
        assert "the%20latest" in page.url.lower(), f"URL {page.url} does not contain 'the-latest'"
