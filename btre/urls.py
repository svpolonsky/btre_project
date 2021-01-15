from django.contrib import admin
#from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from .sitemap import sitemaps
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('',include('pages.urls')),
    path('listings/',include('listings.urls')),
    path('accounts/',include('accounts.urls')),
    path('owners/',include('owners.urls')),
    path('records/',include('records.urls')),
    path('contacts/',include('contacts.urls')),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('sitemap.xml', sitemap,{'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("yandex_748235101bd5901c.html",TemplateView.as_view(template_name="yandex_748235101bd5901c.html", content_type="text/html")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

