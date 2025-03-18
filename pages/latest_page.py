from pages.base_page import BasePage


class LatestPage(BasePage):
    """The Latest page object for the Y Combinator website"""

    def __init__(self, page):
        """Initialize the LatestPage with selectors"""
        super().__init__(page)

        # Updated selectors for the carousel items
        self.gpt_article = ".library-preview-default:has-text('GPT-4.5')"
        self.last_article = ".library-preview-default:last-child"
        self.last_article_title = ".library-preview-default:last-child .font-bold"

        # Updated TOC selectors based on the provided HTML
        self.table_of_contents = ".prose.prose-sm h2:text('Chapters')"
        self.toc_items = ".prose.prose-sm .mb-1.flex.text-sm"

    def navigate_to_latest(self):
        """Navigate directly to The Latest page"""
        self.navigate_to("library/carousel/The%20Latest")
        # Wait for the carousel to load
        self.wait_for_element(".carousel")

    def click_gpt_article(self):
        """Click on the first article that starts with 'GPT-4.5'"""
        # Wait for carousel to load
        self.wait_for_element(".carousel")

        # Use the same pattern as first_article but with GPT-4.5 text
        gpt_article = self.page.query_selector(self.gpt_article)

        if gpt_article:
            print("Found GPT-4.5 article")
            gpt_article.click()
        else:
            raise Exception("No article found with title starting with 'GPT-4.5'")

        self.page.wait_for_load_state("networkidle")

    def get_last_article_title(self):
        """Get the title of the last article after scrolling to the bottom"""
        self.scroll_to_bottom()
        self.wait_for_element(self.last_article)
        self.scroll_to_element(self.last_article_title)
        title = self.get_element_text(self.last_article_title)
        print(f"Last article title: {title}")
        return title

    def get_article_toc_items(self):
        """Get all table of contents items from the current article"""
        try:
            # Wait for page to load and possibly show TOC
            self.page.wait_for_timeout(2000)

            # Check if TOC exists first
            if self.is_element_visible(self.table_of_contents, timeout=5000):
                return self.page.query_selector_all(self.toc_items)
            else:
                print("No chapters/TOC found on this page")
                return []
        except Exception as e:
            print(f"Error in get_article_toc_items: {e}")
            return []

    def get_toc_chapters_text(self):
        """Get the text of each TOC chapter"""
        chapters = []
        toc_items = self.get_article_toc_items()

        for item in toc_items:
            # Extract the chapter title (in the "font-medium" div)
            chapter_title = item.query_selector(".font-medium")
            if chapter_title:
                chapters.append(chapter_title.text_content())

        return chapters
