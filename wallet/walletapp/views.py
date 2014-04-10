from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
# Create your views here.


def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('dash_index'))
