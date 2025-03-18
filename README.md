# Y Combinator Website Automation Tests

This project contains automated tests for the Y Combinator website using Playwright with Python and pytest.

## Test Cases

1. **Navigating to the Library Link**: Automate navigation to the "Library" section from the homepage.
2. **Navigating to "The Latest" Section**: Select the "The Latest" section within the Library to display recent content.
3. **Extracting the Table of Contents from Articles**: For the first article in "The Latest," extract and verify the table of contents.
4. **Extracting the Title of the Last Content Item**: Scroll to the bottom of "The Latest" page and extract the title of the last content item.
5. **Verifying the "Apply" Button Functionality**: Click the "Apply" button on the homepage, confirm navigation to the application page, and verify that the expected content is loaded.

## Setup Instructions

### Prerequisites

- Python 3.11
- pip

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ycombinator-test-automation
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```
   playwright install chromium webkit
   ```

### Running Tests

Run tests on all specified browsers (Chromium and WebKit):
```
pytest
```

Run tests on a specific browser:
```
pytest --browser chromium
pytest --browser webkit
```

## Project Structure

- `conftest.py`: Pytest configuration
- `pages/`: Page objects following the Page Object Model pattern
- `tests/`: Test cases organized by functionality

## Group Members

- Ken Maeda
