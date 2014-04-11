from django.conf.urls import *
from .views import *

urlpatterns = patterns('walletapp.views',
    url(r'^$', 'index' , name="dash_index"),
    url(r'^repository/(?P<ident>\d+)$', 'repository', name="issues"),
    url(r'^repositories/$', RepositoriesView.as_view(), name="repositories"),
)

urlpatterns += patterns(
    'walletapp.controllers',
    url(r'^auth/', include('social_auth.urls')),
    url(r'^logout/$', logoutView, name="logout")
)
