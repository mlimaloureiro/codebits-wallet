from django.db import models
from django.contrib.auth.models import User

class Repositories(models.Model):
	name = models.CharField(max_length=200)
	fullname = models.CharField(max_length=400)
	url = models.CharField(max_length=400)
	description = models.CharField(max_length=2000)
	github_id = models.CharField(max_length=100)

class Proposition(models.Model):
    user = models.ForeignKey(User)
    repositories = models.ForeignKey(Repositories)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField()

