# board/forms.py

from django import forms
from .models import Post



#def min_length_3_validator(value):
#	if len(value) < 3:
#		raise forms.ValidationError('plz Writing more than 3 length')

class PostForm(forms.ModelForm):
	#title = forms.CharField(validators=[min_length_3_validator])
	#content = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Post
		fields = '__all__'
		#fields = ['title', 'content', 'user_agent']
		widgets = {
			'user_agent': forms.HiddenInput,
		}
'''
	def save(self, commit=True):
		post = Post (**self.cleaned_data)
		if commit:
			post.save()
		return post
'''