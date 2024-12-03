AUTHOR = 'Edward Qin'
SITENAME = 'Edwardme'
SITEURL = ''
TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'zh-CN'

SUBTITLE = 'Welcome!'
SUBTEXT = '''
这里是Edward Qin的Blog <br>
欢迎订阅<br>
'''
COPYRIGHT = '©2024 Edward Qin'
PATH = 'content'
THEME = 'themes/Papyrus'
THEME_STATIC_PATHS = ['static']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['readtime', 'search', 'neighbors', 'pelican-toc']
STATIC_PATHS = [
    'images',
    'images/favicon.ico',
    'extra/robots.txt',
    ]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'images/favicon.ico': {'path': 'favicon.ico'},
    }

DISPLAY_PAGES_ON_MENU = True
DIRECT_TEMPLATES = (('index', 'search', 'tags', 'categories', 'archives',))
PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None, 'archives': 24, }

# Site search plugin
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"
# Table of Content Plugin
TOC = {
    'TOC_HEADERS': '^h[1-3]',   # What headers should be included in
                                # the generated toc
                                # Expected format is a regular expression
    'TOC_RUN': 'true',    # Default value for toc generation,
                          # if it does not evaluate
                          # to 'true' no toc will be generated
    'TOC_INCLUDE_TITLE': 'false',    # If 'true' include title in toc
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RSS_FEED_SUMMARY_ONLY = True

# Social widgets 改成您自己的社交账号
SOCIAL = (
    ('github', 'https://github.com/edwardqin-creator'),
    ('twitter', 'https://twitter.com/'),
    ('instagram', 'https://instagram.com/')
)

# Article share widgets
SHARE = (
    ("twitter", "https://twitter.com/intent/tweet/?text=Features&amp;url="),
    ("linkedin", "https://www.linkedin.com/sharing/share-offsite/?url="),
    ("reddit", "https://reddit.com/submit?url="),
    ("facebook", "https://facebook.com/sharer/sharer.php?u="),
    ("whatsapp", "https://api.whatsapp.com/send?text=Features - "),
    ("telegram", "https://telegram.me/share/url?text=Features&amp;url="),
)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# DISQUS_SITENAME = ''
# GOOGLE_ANALYTICS = ''
