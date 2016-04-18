# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='dashboard'),
    url(r'/connect/$', TemplateView.as_view(template_name='connect.html'), name='connect'),
    url(r'/about/$', TemplateView.as_view(template_name='about.html'), name='about'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
