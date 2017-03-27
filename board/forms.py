# board/forms.py

from django import forms

def min_length_3_validator(value):
	if len(value) < 3:
		raise forms.ValidationError('plz Writing more than 3 length')

class PostForm(forms.Form):
	titme = forms.charField(validators=[min_length_3_validator])
	content = forms.charField(widget=forms.Textarea)
