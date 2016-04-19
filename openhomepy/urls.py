# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from core.views import HomepageView, ConnectView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name='dashboard'),
    url(r'connect/$', ConnectView.as_view(), name='connect'),
    url(r'about/$', TemplateView.as_view(template_name='about.html'), name='about'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
