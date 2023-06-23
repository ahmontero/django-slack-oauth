# -*- coding: utf-8 -*-

try:
    from django.urls import path
except ImportError:
    from django.conf.urls import url as path

from .views import SlackAuthView, DefaultSuccessView


urlpatterns = [
    path('login/', SlackAuthView.as_view(), name='slack_auth'),
    path('success/', DefaultSuccessView.as_view(), name='slack_success')
]
