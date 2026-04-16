AUTHOR = '[Your Name]'
SITENAME = 'Pelican Tutorial'
SITEURL = "https://chenkianwee.github.io/pelican_tutorial"

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'themes/simple_bootstrap5' # default was 'notmyidea'

DELETE_OUTPUT_DIRECTORY = True  # default was False
SLUGIFY_SOURCE = 'basename'  # default was 'title'

INDEX_SAVE_AS = '/blogs/index.html'  # default was 'index.html'
ARTICLE_PATHS = ['blogs']  # default was ['']
PAGE_PATHS = ['pages']  # default was ['pages']

USE_FOLDER_AS_CATEGORY = False  # default was True
PATH_METADATA = r'(?P<path_no_ext>.*)\..*'  # default was ''
ARTICLE_URL = '{path_no_ext}.html'  # default was '{slug}.html'
PAGE_URL = '{path_no_ext}.html'  # default was 'pages/{slug}.html'
ARTICLE_SAVE_AS = '{path_no_ext}.html'  # default was '{slug}.html'
PAGE_SAVE_AS = '{path_no_ext}.html'  # default was 'pages/{slug}.html'

ARCHIVES_SAVE_AS = False
DISPLAY_CATEGORIES_ON_MENU = False

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

MENUITEMS = (
    ("Home", f"{SITEURL}/"),
    ("Blog", f"{SITEURL}/blogs/"),
    ("About", f"{SITEURL}/pages/about.html"),
)