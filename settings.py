import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
)

MANAGERS = (
)

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(PROJECT_ROOT, 'dev.db')             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
APPEND_SLASH = True

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'r0&mb4p30-f&jj@$zjoy2)@bo%oiq&ax-rr0ja=cic5qvp-ekv'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'middleware.UnderConstructionMiddleware',
    'django.middleware.http.SetRemoteAddrFromForwardedFor',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.redirects',
    'django.contrib.sitemaps',
    'django.contrib.comments',
    'django.contrib.markup',
    'django_ext',
    'django_memcached',
    'pagination',
    'south',
    'django_extensions',
    
    'piston',
    'api',
    'basic',
    'basic.blog',
    'basic.inlines',
    'contact_form',
    'flatblocks',
    'native_tags',
    'staff',
    'template_utils',
    'mptt',
    'mptt_comments',
    'frontendadmin',
    'categories',
    'requirements',
    'terminal',
    'events',
    
    'tinymce',
    'tagging',
)

TINYMCE_ADMIN_FIELDS = {
    'blog.post': ('body',),
    'flatpages.flatpage': ('content',),
    'flatblocks.flatblock': ('content',),
    'staff.staffmember': ('bio',),
    'events.event': ('description',)
}

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'relative_urls': False,
    'plugins' : "safari,spellchecker,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'theme_advanced_buttons1' : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2' : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
    'theme_advanced_buttons3' : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl,|,fullscreen",
    'theme_advanced_buttons4' : "insertlayer,moveforward,movebackward,absolute,|,styleprops,spellchecker,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,blockquote,pagebreak,|,insertfile,insertimage",
    'theme_advanced_statusbar_location' : "bottom",
    'width': "97%",
}


FRONTEND_FORMS = {
    'blog.post': 'django_ext.forms.PostForm',
    'flatpages.flatpage': 'django_ext.forms.FlatPageForm',
    'flatblocks.flatblock': 'django_ext.forms.FlatBlockForm',
    'events.event': 'django_ext.forms.EventForm',
}

def get_flatblock(context, **lookup):
    from flatblocks.models import FlatBlock
    try:
        return FlatBlock.objects.get(**lookup)
    except FlatBlock.DoesNotExist:
        return
get_flatblock.takes_context = True

def get_home_flatblock(context):
    return get_flatblock(context, slug='home')
get_home_flatblock.takes_context = True

def get_images():
    from random import shuffle
    I="""http://lh6.ggpht.com/_f3gaky_MG94/S-SkIEEF_AI/AAAAAAAAAvM/fPib5m_NA6k/s1024/Picture%20018.jpg
    http://lh5.ggpht.com/_f3gaky_MG94/S-SkNF6MdjI/AAAAAAAAAvU/y8zUKzy-0i4/s1024/Picture%20020.jpg
    http://lh5.ggpht.com/_f3gaky_MG94/S-SkSf8vroI/AAAAAAAAAvY/HuUtOTEgZ8I/s1024/Picture%20024.jpg
    http://lh3.ggpht.com/_f3gaky_MG94/S-SkWBFCX5I/AAAAAAAAAvg/gJTnCDxy26k/s1024/Picture%20036.jpg
    http://lh5.ggpht.com/_f3gaky_MG94/S-Ska9X1FnI/AAAAAAAAAvk/3Wbqggo5s2I/s1024/Picture%20038.jpg
    http://lh4.ggpht.com/_f3gaky_MG94/S-SkgG9recI/AAAAAAAAAvs/iSnHNcqFsNM/s1024/Picture%20049.jpg
    http://lh4.ggpht.com/_f3gaky_MG94/S-SklR4OzyI/AAAAAAAAAvw/_1Wl7pPkIfU/s1024/Picture%20054.jpg
    http://lh4.ggpht.com/_f3gaky_MG94/S-SkqlaRjVI/AAAAAAAAAv0/WIA0kAP7sWk/s1024/Picture%20074.jpg
    http://lh4.ggpht.com/_f3gaky_MG94/S-SkwAlP1-I/AAAAAAAAAv4/yFZ7FOWdPak/s1024/Picture%20075.jpg""".splitlines()
    shuffle(I)
    return I

NATIVE_LIBRARY = {
    'function':{
        'get_home_flatblock': get_home_flatblock,
        'get_flatblock': get_flatblock,
        'get_images':get_images,
    }
}

SOUTH_AUTO_FREEZE_APP = True

DJANGO_MEMCACHED_REQUIRE_STAFF = True

CACHE_BACKEND = 'dummy:///'

try:
    from local_settings import *
except ImportError:
    pass
