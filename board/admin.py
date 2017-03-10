from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

#admin.site.register(Post, PostAdmin)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'content_size','created_at', 'updated_at']

	def content_size(self, post):
		#return '{} length'.format(len(post.content))
		return mark_safe('<strong>{}</string>length'.format(len(post.content)))