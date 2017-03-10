from __future__ import unicode_literals
from django.db import models
from django.forms import ValidationError

def content_validator(value):
	if len(value) < 10:
		raise ValidationError('Please enter more than 10 characters')

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(validators=[content_validator])
	tags = models.CharField(max_length=100, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

