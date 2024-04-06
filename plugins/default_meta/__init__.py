from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options
import os

class DefaultMetaPlugin(BasePlugin):
    # A mapping for special case language names
    SPECIAL_CASES = {
        'typescript': 'TypeScript',
        'javascript': 'JavaScript',
        'csharp': 'C#',
        'objective-c': 'Objective-C',
    }

    def format_language_name(self, filename):
        """Format language name correctly based on filename."""
        language = os.path.splitext(filename)[0]
        return self.SPECIAL_CASES.get(language, language.capitalize())

    def on_page_markdown(self, markdown, page, config, files):
        # Basic site info
        site_url = config.get('site_url', 'https://styles.goatbytes.io')
        default_image = f"{site_url}assets/img/social.jpg"

        # Extract and format the language name from the file name
        language = self.format_language_name(os.path.basename(page.file.src_path))
        custom_title = f"{language} Code Style Guide | GoatStyles"
        custom_description = f"The official {language} code style guide used by GoatBytes.IO."

        # Default meta tags with dynamic title and description
        defaults = [
            {'name': 'description', 'content': custom_description},
            {'property': 'og:type', 'content': 'website'},
            {'property': 'og:title', 'content': custom_title},
            {'property': 'og:description', 'content': custom_description},
            {'property': 'og:image', 'content': default_image},
            {'property': 'og:url', 'content': site_url},
            {'name': 'twitter:card', 'content': 'summary_large_image'},
            {'name': 'twitter:title', 'content': custom_title},
            {'name': 'twitter:description', 'content': custom_description},
            {'name': 'twitter:image', 'content': default_image},
        ]

        # Initialize or update page meta
        if 'meta' not in page.meta:
            page.meta['meta'] = defaults
        else:
            # Update existing tags or add defaults if missing
            existing_tags = {tag.get('name') or tag.get('property'): tag for tag in page.meta['meta']}
            for default in defaults:
                key = default.get('name') or default.get('property')
                if key not in existing_tags:
                    page.meta['meta'].append(default)
                elif key in ['description', 'og:title', 'og:description', 'twitter:title', 'twitter:description']:
                    # Update content for specific tags if they already exist
                    existing_tags[key]['content'] = default['content']

        return markdown
