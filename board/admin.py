from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Comment, Tag

#admin.site.register(Post, PostAdmin)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'user', 'title', 'content_size', 'subjects', 'created_at', 'updated_at']

	actions = ['make_ros', 'make_ruby', 'make_html', 'make_js', 'make_python', 'make_ol']

	def content_size(self, post):
		#return '{} length'.format(len(post.content))
		return mark_safe('<strong>{}</string>length'.format(len(post.content)))

	def make_ros(self, request, queryset):
		updated_count = queryset.update(subjects='R1') # QuerySet.update
		self.message_user(request, '{} Changed RubyOnRails'.format(updated_count))
	make_ros.short_description = 'Changed RubyOnRails'

	def make_ruby(self, request, queryset):
		updated_count = queryset.update(subjects='R2') # QuerySet.update
		self.message_user(request, '{} Changed Ruby'.format(updated_count))
	make_ruby.short_description = 'Changed Ruby'

	def make_html(self, request, queryset):
		updated_count = queryset.update(subjects='H') # QuerySet.update
		self.message_user(request, '{} Changed HTML'.format(updated_count))
	make_html.short_description = 'Changed HTML'

	def make_js(self, request, queryset):
		updated_count = queryset.update(subjects='J') # QuerySet.update
		self.message_user(request, '{} Changed JS'.format(updated_count))
	make_js.short_description = 'Changed JS'

	def make_python(self, request, queryset):
		updated_count = queryset.update(subjects='P') # QuerySet.update
		self.message_user(request, '{} Changed Python'.format(updated_count))
	make_python.short_description = 'Changed Python'

	def make_ol(self, request, queryset):
		updated_count = queryset.update(subjects='O') # QuerySet.update
		self.message_user(request, '{} Changed Other Language'.format(updated_count))
	make_ol.short_description = 'Changed Other Language'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	pass