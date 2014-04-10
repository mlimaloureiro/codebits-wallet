from django.db import models
from django.contrib.auth.models import User

class Proposition(models.Model):
    user = models.ForeignKey(User)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)