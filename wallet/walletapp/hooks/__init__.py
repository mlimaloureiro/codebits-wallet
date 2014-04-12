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
from django.views.decorators.csrf import csrf_exempt
import requests
import datetime


def test_hook(repository='https://api.github.com/repos/andreesg/goncalves.me', hook_id=2085891, token="498e024392092d9f202adf21edfa1167e256772f"):
    # Build request url
    url = repository+"/hooks/"+str(hook_id)+"/tests"
    headers = {"Authorization": "token "+str(token)}

    # Make the test push request
    r = requests.post(url, headers=headers)

    # Check if succeded
    if r.status_code != 204:
        return HttpResponse(json.dumps({"success":False}))
    else:
        return HttpResponse(json.dumps({"success":True}))


def create_hook(repository='https://api.github.com/repos/andreesg/goncalves.me', token="498e024392092d9f202adf21edfa1167e256772f"):
    # Create Webhook request
    hook = {
        'name': 'web',
        'active': True,
        'config': {
            'url': 'http://codingbooster.herokuapp.com/hooks/',
            'content_type': 'json'
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
        return False
    else:
        # SAVE HOOK ID
        hook_id = response["id"]
        return {'hook_id':hook_id, 'hook_url' : response['url']}


# Handle Github Webhooks
@csrf_exempt
def receive_hook(request):
    try:
        event = request.META['HTTP_X_GITHUB_EVENT']
        if event == "pull_request":
            print "pull_request received"
            r = requests.post("http://moth.dec.uc.pt/codebits_hook/", data=json.dumps({"action":"wallet"}))
    except Exception as e:
        return HttpResponse(json.dumps({"success":False, "error_msg": "Github header not found."}))
    else:
        return HttpResponse(json.dumps({"success":True}))

def create_user_payments(issue_url, user):
    propositions = Proposition.objects.filter(issue_id=issue_url)
    if len(propositions) > 0:
        total_amount = 0
        for proposition in propositions:
            total_amount += proposition.value
            proposition.status = DONE
            proposition.save()

        email = get_user_email(user)
        print "user email: "+email
        return True
    else:
        return False

def get_user_email(login):
    r = requests.get("https://api.github.com/users/"+login)
    response = r.json()
    email = response["email"]

    return email

# Handle pull request
def handle_pull_request(raw_data):
    print "handle pull request"

    data = json.loads(raw_data)
    pull_request = data["pull_request"]
    user = data["head"]["user"]["login"]
    print "get user url: "+user

    # Check if merged and closed
    # Check if issue is related to some user
    if data['action'] == "closed":
        print "pull_request action: closed."
        if pull_request['merged'] == True:
            if create_user_payments(pull_request['issue_url'], user):
                print "created payment"
                return True
    else:
        print "pull_request action: "+data["action"]
        return False

    # Send to wallet
    return False

