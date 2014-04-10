from django.conf.urls import *
from .views import logoutView

urlpatterns = patterns(
    'walletapp.controllers',
    url(r'^$', 'dash.index', name="dash_index"),
    url(r'issues$', 'dash.get_issues'),
    url(r'^auth/', include('social_auth.urls')),
    url(r'^logout/$', logoutView, name="logout")
)
