from django.conf.urls import url

from pattern_library import (
    get_pattern_template_prefix, get_pattern_template_suffix, views
)

app_name = 'pattern_library'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^display/type/(?P<pattern_type>[\w]+)/$', views.IndexView.as_view(), name='display_by_type'),
    url(
        r'^display/pattern/(?P<template_name>%s/[\w./-]+%s)$' % (
            get_pattern_template_prefix(), get_pattern_template_suffix()
        ),
        views.PatternView.as_view(),
        name='display_pattern'
    ),
]
