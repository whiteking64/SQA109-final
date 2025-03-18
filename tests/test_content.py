from pages.latest_page import LatestPage


# Test Case 3: Extracting the Table of Contents from a specific article
def test_extract_table_of_contents(page):
    """
    Test Case 3: Extracting the Table of Contents from a specific article

    Steps:
    1. Navigate to 'The Latest' page
    2. Click on the article with title starting with 'GPT-4.5'
    3. Extract the table of contents
    4. Verify that the table of contents exists and has items
    """
    # Arrange
    latest_page = LatestPage(page)

    # Act
    latest_page.navigate_to_latest()
    latest_page.click_gpt_article()
    toc_items = latest_page.get_article_toc_items()

    # Assert
    assert len(toc_items) > 0, "No table of contents items found"

    # Verify each TOC item has text
    for item in toc_items:
        item_text = item.text_content().strip()
        assert item_text, f"TOC item has no text: {item}"
        print(f"TOC item: {item_text}")


# Test Case 4: Extracting the Title of the Last Content Item
def test_extract_last_content_title(page):
    """
    Test Case 4: Extracting the Title of the Last Content Item

    Steps:
    1. Navigate to 'The Latest' page
    2. Scroll to the bottom of the page
    3. Extract the title of the last content item
    4. Verify that the title exists
    """
    # Arrange
    latest_page = LatestPage(page)

    # Act
    latest_page.navigate_to_latest()
    last_title = latest_page.get_last_article_title()

    # Assert
    assert last_title, "Last article title is empty"
    print(f"Last article title: {last_title}")
