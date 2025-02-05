AUTHOR = "Pedro Luis Boll Lugo"
SITENAME = "Peterjuse Bizarre Adventure"
SITESUBTITLE = "Mi intento de blog personal sobre lo que venga"
SITEURL = "http://peterjuse.github.io"
TIMEZONE = "America/Caracas"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

GITHUB_URL = "http://github.com/peterjuse/"
DISQUS_SITENAME = "peterjuse-blog"
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2025, 1, 19, 12, 0, 0)

FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

LINKS = (
    ("Gentecnologico", "http://gentecnologico.wordpress.com"),
)

SOCIAL = (
    ("X", "http://x.com/pedro_luis22"),
    ("Instagram", "https://instagram.com/pedro_luis22"),
    ("github", "http://github.com/peterjuse"),
)

# global metadata to all the contents
DEFAULT_METADATA = {"yeah": "it is"}

# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    "images",
    "extra/robots.txt",
]

# custom page generated with a jinja2 template
TEMPLATE_PAGES = {"pages/jinja2_template.html": "jinja2_template.html"}

# there is no other HTML content
READERS = {"html": None}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {"linenos": "table"}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"

#Custom Home page
DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
PAGINATED_TEMPLATES = (('blog',))
TEMPLATE_PAGES = {'home.html': 'index.html',}

THEME = 'themes/bootstrap2'
OUTPUT_PATH = 'output'
PATH = 'content'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
