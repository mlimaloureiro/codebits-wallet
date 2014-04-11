from django.shortcuts import render
from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.views.generic import View, DetailView
from braces.views import JSONResponseMixin
from walletapp.models import *
import simplejson as json
from django.core.serializers import serialize
import requests
import datetime
# Create your views here.


def index(request):
    opts = {}
    t = loader.get_template('base.html')
    return HttpResponse(t.render(RequestContext(request, opts)))

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('dash_index'))

class RepositoriesView(JSONResponseMixin, View):
	model = Repositories
	json_dump_kwargs = {u"indent":2}
	content_type = u"application/javascript"

	def get(self, request, *args,**kwargs):		
		response = serialize('json', self.model.objects.all())
		return self.render_json_response(json.loads(response))

