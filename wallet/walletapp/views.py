from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.views.generic import View, DetailView, UpdateView, CreateView, RedirectView
from braces.views import JSONResponseMixin, JsonRequestResponseMixin, LoginRequiredMixin
from walletapp.models import *
from django.core.serializers import serialize
from walletapp.hooks import *
import simplejson as json
import requests
import datetime

from django.contrib import messages

from .forms import UserForm, PropositionForm
# Create your views here.


def index(request):
    t = loader.get_template('repositories.html')
    return HttpResponse(t.render(RequestContext(request, {})))

def repository(request, ident):
    obj = Repositories.objects.get(id = ident)
    t = loader.get_template('issues.html')
    return HttpResponse(t.render(RequestContext(request, {'repo':obj})))

def myRepositories(request):
    myRepos = serialize('json',Repositories.objects.filter(
        user = User.objects.get(id = int(request.user.id))))

    return HttpResponse(json.dumps(myRepos), content_type="json")


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

class RepositoriesView(JsonRequestResponseMixin, View):
    model = Repositories
    json_dump_kwargs = {u"indent":2}
    content_type = u"application/javascript"

    def get(self, request, *args, **kwargs):
        response = serialize('json', self.model.objects.all())
        return self.render_json_response(json.loads(response))

    def post(self, request, *args, **kwargs):
        owner = request.POST['owner']
        repo = request.POST['repo']
        u = User.objects.get(id = request.user.id)
        token = u.social_auth.filter(provider = 'github')[0].extra_data['access_token']

        url = 'https://api.github.com/repos/' + owner + '/' + repo

        hook = create_hook(url, token)

        if hook:
            Repositories.objects.create(name = owner + '/' + repo ,
                fullname = owner + '/' + repo,
                url = 'http://github.com/' + owner + '/' + repo,
                total_propositions = 0,
                user_id = request.user.id,
                hook_id = hook['hook_id'],
                hook_url = hook['hook_url'])

            return HttpResponse(json.dumps({"success":True}))
        else:
            return HttpResponse(json.dumps({"success":False}))


class FavouritesView(JSONResponseMixin,View):
    model = Favourites
    json_dump_kwargs = {u"indent":2}
    content_type = u"application/javascript"

    def get(self, request, *args,**kwargs):
        response = serialize('json', self.model.objects.all())
        return self.render_json_response(json.loads(response))


class CreatePropositionView(LoginRequiredMixin, CreateView):
    model = Proposition
    form_class = PropositionForm

    def form_valid(self, form):
        prop = Proposition(**form.cleaned_data)
        prop.user = self.request.user
        prop.save()
        user = self.request.user

        data = {
            "payment": {
                "client": {
                   "name": " ".join([user.first_name, user.last_name]),
                   "email": user.email,
                },
                "amount": prop.value/100.0,
                "currency": "EUR",
            },
            "url_confirm": reverse_lazy('success_proposition'),
            "url_cancel": reverse_lazy('failed_proposition')
        }
        url = "https://wallet.codebits.pt/api/v2/checkout"
        headers = {"Authorization": "WalletPT "+settings.WALLET_MER_ID}
        response = requests.post(url, params=json.dumps(data), headers=headers)
        return HttpResponseRedirect(response.json()["url_redirect"])


class FailedPropositionView(LoginRequiredMixin, RedirectView):

    def get(request, *args, **kwargs):
        messages.error(request, "Unable to transfer funds")
        return HttpResponseRedirect(reverse_lazy('dash_index'))


class SuccessPropositionView(LoginRequiredMixin, RedirectView):

    def get(request, *args, **kwargs):
        messages.success(request, "Proposition created with success")
        return HttpResponseRedirect(reverse_lazy('dash_index'))
