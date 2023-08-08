from django import forms

class StudentRegistration(forms.Form) :
	name = forms.CharField()
	marks = forms.IntegerField()

	# only these fields will reflect on form
	