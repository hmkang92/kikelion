# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Profile
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SignupForm(UserCreationForm):

	phone_number = forms.CharField()
	department = forms.CharField()
	student_number = forms.CharField()

	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ('email',)

	def save(self):
		#user = super().save()
		user = super(SignupForm, self).save()
		profile = Profile.objects.create(
			user = user,
			phone_number = self.cleaned_data['phone_number'],
			department = self.cleaned_data['department'],
			student_number = self.cleaned_data['student_number'])
		return user
		
		
class LoginForm(AuthenticationForm):
	answer = forms.CharField(label='건양대학교 총장님 성함은?')

	def clean_answer(self):
		answer = self.cleaned_data.get('answer', None)
		if answer != '김희수':
			raise forms.ValidationError('건양대학교 학생이 아닌 것 같은데... who a u ?')
		return answer

