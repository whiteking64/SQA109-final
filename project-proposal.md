# Website URL:
- https://www.ycombinator.com/

# Use Cases:
1. Navigating to the Library Link: Automate navigation to the "Library" section from the homepage.
2. Navigating to the "The Latest" Section: Select the "The Latest" section within the Library to display recent content.
3. Extracting the Table of Contents from a specific article: For the first article that starts with "GPT-4.5", extract and verify the table of contents.
4. Extracting the Title of the Last Content Item: Scroll to the bottom of "The Latest" page and extract the title of the last content item.
5. Verifying the "Apply" Button Functionality: Click the "Apply" button on the homepage, confirm navigation to the application page, and verify that the expected content (there will be another button) is loaded.

# Locator Strategies:
- Navigation Elements: Identify and interact with navigation tabs using link text or CSS selectors.
- Article Links and Content: Use CSS selectors to locate article elements and their respective sections.
- Scrolling Actions: Utilize Playwright's page interaction methods to simulate scrolling.
- "Apply" Button: Locate and click the "Apply" button using text or a unique CSS selector.
- Application Page Verification: Verify the presence of key elements such as headings or the button.

# Browser Compatibility:
- Chromium (Google Chrome) and WebKit (Safari)

# Group Members:
- Ken Maeda

# Test Framework and Language:
- Framework: Playwright integrated with Pytest
- Language: Python
