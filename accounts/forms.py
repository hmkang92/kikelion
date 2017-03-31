from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):

	phone_number = forms.CharField()
	department = forms.CharField()
	student_number = forms.CharField()

	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ('email',)

	def save(self):
		user = super().save()
		profile = Profile.objects.create(
			user = user,
			phone_number = self.cleaned_data['phone_number'],
			department = self.cleaned_data['department'],
			student_number = self.cleaned_data['student_number'])
			
		return user
		
		


