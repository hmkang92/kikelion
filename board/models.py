from __future__ import unicode_literals
from django.db import models
from django.forms import ValidationError

def content_validator(value):
	if len(value) < 10:
		raise ValidationError('Please enter more than 10 characters')

class Post(models.Model):
	SUBJECTS_CHOICES = (
		('R1', 'Rails'),
		('R2', 'Ruby'),
		('H', 'HTML'),
		('J', 'JS'),
		('P', 'PY'),
		('O', 'Other'),

	)

	author = models.CharField(max_length=20)
	title = models.CharField(max_length=100)
	content = models.TextField(validators=[content_validator])
	tags = models.CharField(max_length=100, blank=True)
	subjects = models.CharField(max_length=1, choices=SUBJECTS_CHOICES)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)



	def __unicode__(self):
		return self.title