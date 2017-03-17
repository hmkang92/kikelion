# accounts/models.py
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User)
	student_number = models.CharField(max_length=10)
	department = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=20)
