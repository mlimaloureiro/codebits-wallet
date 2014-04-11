from django.db import models
from django.contrib.auth.models import User


class Repositories(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    fullname = models.CharField(max_length=400)
    url = models.CharField(max_length=400)
    description = models.CharField(max_length=2000)
    github_id = models.CharField(max_length=100)
    hook_id = models.CharField(max_length=100)
    hook_url = models.CharField(max_length=300)
    total_propositions = models.IntegerField(default = 0)


WAITING = 0
FAILED = 1
ACTIVE = 2
RETURNED = 3
DONE = 4

PROP_STATUSES = (
    (WAITING, 'Waiting'),
    (FAILED, 'Failed'),
    (ACTIVE, 'Active'),
    (RETURNED, 'Returned'),
    (DONE, 'Done'),
)


class Proposition(models.Model):
    user = models.ForeignKey(User)
    repository = models.ForeignKey(Repositories)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    issue_id = models.CharField(max_length=300)
    value = models.IntegerField(default=500)
    status = models.IntegerField(choices=PROP_STATUSES, default=WAITING)
    expires = models.DateTimeField(null=True, blank=True)


class Favourites(models.Model):
    user = models.ForeignKey(User)
    repository = models.ForeignKey(Repositories)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField()
