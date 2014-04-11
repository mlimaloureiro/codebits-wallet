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


def test_hook(repository='https://api.github.com/repos/andreesg/goncalves.me', hook_id=2085891, token="498e024392092d9f202adf21edfa1167e256772f"):
    # Build request url
    url = repository+"/hooks/"+str(hook_id)+"/tests"
    headers = {"Authorization": "token "+str(token)}

    # Make the test push request
    r = requests.post(url, headers=headers)
    response = r.json()

    # Check if succeded
    if r.status_code != 204:
        return HttpResponse(json.dumps({"success":False, "response":response}))
    else:
        return HttpResponse(json.dumps({"success":True}))


def create_hook(repository='https://api.github.com/repos/andreesg/goncalves.me', token="498e024392092d9f202adf21edfa1167e256772f"):
    # Create Webhook request
    hook = {
        'name': 'web',
        'active': True,
        'config': {
            'url': 'http://moth.dec.uc.pt/codebits_hook/',
            'content_type': 'json',
        },
        'events': [
            'push',
            'pull_request'
        ]
    }

    # Add auth token to header
    headers = {"Authorization": "token "+str(token)}
    url = repository+"/hooks"

    # Send request and parse response
    r = requests.post(url, headers=headers, data=json.dumps(hook))
    response = r.json()

    # Check if the request was successfull
    if r.status_code != 201:
        return HttpResponse(json.dumps({"success":False, "response":response}))
    else:
        # SAVE HOOK ID
        hook_id = response["id"]
        return HttpResponse(json.dumps({"success":True, "hook_id":hook_id, "hook_url":response["url"]}))

# Handle Github Webhooks
def receive_hook(request):
    try:
        event = request.META['HTTP_X_GITHUB_EVENT']
        if event is "pull_request":
            handle_pull_request(request.body)
    except Exception as e:
        return HttpResponse(json.dumps({"success":False, "error_msg": "Github header not found."}))
    else:
        return HttpResponse(json.dumps({"success":True}))

# Handle pull request
def handle_pull_request(raw_data):
    data = json.loads(raw_data)
    pull_request = data["pull_request"]
    user = data["head"]["user"]["url"]

    # Check if merged and closed
    # Check if issue is related to some user
    if data['action'] == "closed":
        if pull_request['merged'] == True:
            check_user_payments(user, pull_request['issue_url'])

    # Send to wallet
    return {'success':True }

