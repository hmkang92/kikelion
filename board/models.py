from __future__ import unicode_literals
from django.db import models
from django.forms import ValidationError
from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

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
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=100)
	content = models.TextField(validators=[content_validator])
	photo = ProcessedImageField(blank=True, upload_to='board/post/%Y/%m/%d',
		processors=[Thumbnail(300, 300)],
		format='JPEG',
		options={'quality':60})
	user_agent = models.CharField(max_length=200)
	tags = models.CharField(max_length=100, blank=True)
	subjects = models.CharField(max_length=1, choices=SUBJECTS_CHOICES)
	tag_set = models.ManyToManyField('Tag', blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ['-id']

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('board:post_detail', args=[self.id])



class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.CharField(max_length=20)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


#In [1]: Post
#Out[1]: board.models.Post

#In [2]: Post.objects.filter(tag_set__name='django')
#Out[2]: <QuerySet [<Post: 123>]>

#In [3]: Post.objects.filter(tag_set__name='Ruby')
#Out[3]: <QuerySet [<Post: 123>]>

#In [4]: Post.objects.filter(tag_set__name__in=['django', 'Ruby'])
#Out[4]: <QuerySet [<Post: 123>, <Post: 123>]>



class Tag(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.name