# Create sitemap for static pages in Django application
# source: https://www.atemon.com/blog/create-sitemap-for-static-pages-in-django-application/

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings

class StaticSitemap(Sitemap):
    protocol = 'https'
    lastmod = settings.LAST_MODIFIED
    changefreq = 'monthly'
    priority_dict = 0.5

    def items(self):
        return [
            "index",
            "about",
        ]

    def location(self, item):
        if isinstance(item, tuple):
            return reverse(item[0], kwargs=item[1])
        return reverse(item)

sitemaps = {
    'static': StaticSitemap,
}