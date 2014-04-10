from django.conf.urls import *
from django.contrib.auth import *

urlpatterns = patterns('walletapp.controllers',
                       (r'^$', 'dash.index'),
                       (r'issues$', 'dash.get_issues'),
                       )
