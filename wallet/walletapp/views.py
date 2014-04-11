from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.views.generic import View, DetailView, UpdateView
from braces.views import JSONResponseMixin
from walletapp.models import *
import simplejson as json
from django.core.serializers import serialize
import requests
import datetime

from .forms import UserForm
# Create your views here.


def index(request):
    t = loader.get_template('repositories.html')
    return HttpResponse(t.render(RequestContext(request, {})))

def repository(request, ident):
    t = loader.get_template('issues.html')
    return HttpResponse(t.render(RequestContext(request, {ident:ident})))


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('dash_index'))


class UserProfileView(UpdateView):
    """Shows and updates user preferences"""
    model = User
    template_name = "profile.html"
    form_class = UserForm

    def dispatch(self, request, *args, **kwargs):
        self.kwargs['pk'] = request.user.pk
        return super(UserProfileView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        #Temp
        return super(UserForm, self).post(request, *args, **kwargs)


class RepositoriesView(JSONResponseMixin, View):
    model = Repositories
    json_dump_kwargs = {u"indent":2}
    content_type = u"application/javascript"

    def get(self, request, *args,**kwargs):
        response = serialize('json', self.model.objects.all())
        return self.render_json_response(json.loads(response))


class FavouritesView(JSONResponseMixin,View):
    model = Favourites
    json_dump_kwargs = {u"indent":2}
    content_type = u"application/javascript"

    def get(self, request, *args,**kwargs):
        response = serialize('json', self.model.objects.all())
        return self.render_json_response(json.loads(response))


