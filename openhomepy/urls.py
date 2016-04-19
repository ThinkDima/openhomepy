# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from core.views import HomepageView, DiscoveredView, ConnectView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='dashboard'),
    url(r'discovered/$', DiscoveredView.as_view(), name='discovered'),
    url(r'about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'connect/(?P<pk>\d+)/$', ConnectView.as_view(), name='connect')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
