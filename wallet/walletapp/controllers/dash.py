#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
import simplejson as json
import datetime

def index(request):
	opts = {}
	t = loader.get_template('dash.html')
	return HttpResponse(t.render(RequestContext(request, opts)))