from django.shortcuts import render
from . import forms

# Create your views here.

def feedbackview(request) :
	if request.method=='GET' :
		form=forms.FeedbackForm()
		return render(request, 'testapp/register.html', {'form':form})
	if request.method=='POST' :
		form = forms.FeedbackForm(request.POST)
		if form.is_valid() :
			print('Form validate success and printing Feedback info')
			print('Student name : ', form.cleaned_data['name'])     # cleaned_data is a predefined variable, store data in dictionary form
			print('Roll no. : ', form.cleaned_data['rollno'])
			print('Mail ID : ', form.cleaned_data['email'])
			print('Feedback : ', form.cleaned_data['feedback'])
			return render(request, 'testapp/thankyou.html', {'name' : form.cleaned_data['name']})

	return render(request, 'testapp/register.html', {'form':form})