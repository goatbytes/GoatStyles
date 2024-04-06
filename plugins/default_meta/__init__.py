from typing import Dict, List, Optional, Tuple
from mkdocs.plugins import BasePlugin
import os


class DefaultMetaPlugin(BasePlugin):
    """
   An MkDocs plugin that automatically generates and updates meta tags
   for pages with enhanced descriptions, keywords, and Open Graph properties.
   """

    LANGUAGES: Dict[str, str] = {
        'cpp': 'C++', 'c': 'C', 'csharp': 'C#', 'css': 'CSS', 'dart': 'Dart', 'go': 'Go',
        'html': 'HTML', 'java': 'Java', 'javascript': 'JavaScript', 'json': 'JSON',
        'kotlin': 'Kotlin', 'markdown': 'Markdown', 'objective-c': 'Objective-C',
        'php': 'PHP', 'python': 'Python', 'ruby': 'Ruby', 'rust': 'Rust', 'scala': 'Scala',
        'shell': 'Shell', 'sql': 'SQL', 'swift': 'Swift', 'typescript': 'TypeScript',
    }

    PAGE_TITLES: Dict[str, str] = {
        'index': 'Home', 'about': 'About', 'contributing': 'Contributing',
        'foundation': 'Foundational Code Standards',
    }

    DEFAULT_KEYWORDS: List[str] = [
        'Coding Standards', 'Programming Best Practices', 'Coding Guidelines',
        'Software Development', 'Code Quality', 'Software Engineering Principles',
        'Code Review Standards', 'Code Style', 'Source Code formatting',
        'Programming Language Style', 'Clean Code Principles', 'Development Guidelines',
        'Best Coding Practices', 'Coding Style Guides', 'Software Craftsmanship',
        'Code Consistency', 'GoatBytes.IO', 'GoatStyles', 'GoatBytes',
    ]

    SITE_DESC: str = ("GoatStyles is an authoritative resource dedicated to promoting "
                      "best practices and consistency in coding across various programming "
                      "languages. As a comprehensive style guide repository created by "
                      "GoatBytes.IO, it aims to elevate code quality and readability for "
                      "developers worldwide.")

    def __init__(self):
        self.site_url: Optional[str] = None
        self.keywords: List[str] = []

    def on_config(self, config):
        """Handles configuration to set site-wide settings."""
        self.site_url = config.get('site_url', 'https://styles.goatbytes.io')
        # Reset keywords to default at the start of each build to avoid accumulation
        self.keywords = self.DEFAULT_KEYWORDS.copy()

    def format_language_name(self, filename: str) -> str:
        """Format language name correctly based on filename."""
        base = os.path.splitext(filename)[0]
        return self.LANGUAGES.get(base, base.capitalize())

    def get_language_keywords(self, language: str) -> List[str]:
        """Generate keywords specific to a programming language."""
        return [
            f"{language} Style Guide",
            f"{language} Syntax Rules",
            f"{language} Coding Conventions"
        ]

    def format_page_title_and_description(self, filename: str) -> Tuple[str, str]:
        """Generate title and description based on filename."""
        base, _ = os.path.splitext(filename)
        if base in self.PAGE_TITLES:
            title = self.PAGE_TITLES[base]
            description = self.SITE_DESC
        elif base in self.LANGUAGES:
            lang = self.LANGUAGES[base]
            # Extend keywords list with language-specific keywords
            self.keywords.extend(self.get_language_keywords(lang))
            title = f"{lang} Code Style Guide"
            description = (f"Explore the official {lang} coding conventions "
                           "and best practices used by GoatBytes.IO.")
        else:
            title = 'GoatStyles Documentation'
            description = self.SITE_DESC
        return title, description

    def on_page_markdown(self, markdown: str, page, config, files) -> str:
        """Add meta tags to page based on content."""
        default_image = f"{self.site_url}/assets/img/goatstyles.png"
        page_title, custom_description = self.format_page_title_and_description(
            os.path.basename(page.file.src_path)
        )

        # Ensure proper formatting and prevent duplication of meta tags
        defaults = self.generate_default_meta(page_title, custom_description, default_image)

        # Initialize or update page meta
        page.meta.setdefault('meta', []).extend(
            [tag for tag in defaults if tag not in page.meta['meta']]
        )

        return markdown

    def generate_default_meta(self, title: str, description: str, image: str) -> List[Dict]:
        """Generates a list of default meta tags."""

        # Ensure the image URL does not have double slashes (except after "http:")
        image = image.replace("//assets", "/assets")
        return [
            {'name': 'description', 'content': description},
            {'name': 'keywords', 'content': ', '.join(self.keywords)},
            {'property': 'og:type', 'content': 'website'},
            {'property': 'og:url', 'content': self.site_url},
            {'property': 'og:site_name', 'content': 'GoatStyles'},
            {'property': 'og:title', 'content': title},
            {'property': 'og:description', 'content': description},
            {'property': 'og:image', 'content': image},
            {'property': 'og:image:type', 'content': 'image/png'},
            {'property': 'og:image:width', 'content': '1200'},
            {'property': 'og:image:height', 'content': '620'},
            {'name': 'twitter:card', 'content': 'summary_large_image'},
            {'name': 'twitter:title', 'content': title},
            {'name': 'twitter:description', 'content': description},
            {'name': 'twitter:image', 'content': image},
        ]
