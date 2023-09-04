from django import forms


class NameForm(forms.Form):
	name = forms.CharField()


class AgeForm(forms.Form):
	age = forms.IntegerField()


class GFForm(forms.Form) :
	gf = forms.CharField()