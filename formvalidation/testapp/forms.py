# implicit validation of form by using Django's inbuilt validators with the help od django.core module


from django import forms
from django.core import validators

def start_with_x(value) :
	if value.isalpha() != True :       # name should only contain alphabets (space also prohibited)
#	if value[0].lower() != 'x' :
		raise forms.ValidationError('name should start with x/X only ')


def gmail_verification(value) :
	if value[len(value)-9:] != 'gmail.com' :
		raise forms.ValidationError("must be gmail")


class FeedbackForm(forms.Form) :
	name = forms.CharField(validators = [start_with_x])
	rollno = forms.IntegerField()
	email = forms.EmailField(validators=[gmail_verification])
	password = forms.CharField()
	rpassword = forms.CharField(label='Password(Again)', widget=forms.PasswordInput)
	feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(88),validators.MinLengthValidator(10)])

	def clean(self) :
		print('password validations')
		cleaned_data = super().clean()
		inputpwd = cleaned_data['password']
		inputrpwd = cleaned_data['rpassword']
		if inputpwd != inputrpwd : 
			raise forms.ValidationError('Password not matched')





"""  validating total form by using single clean() method :

	def clean(self) :
		print('Total form validation..!')
		cleaned_data = super().clean()

		inputname = cleaned_data['name']
		if len(inputname) < 8 :
			raise forms.ValidationError('Name should atleast contain 8 characters')

		inputrollno = cleaned_data['rollno']
		if len(str(inputrollno)) != 3 :
			raise forms.ValidationError('Roll no should compulsory contains exact 3 digits only')

		inputemail = cleaned_data['email']
		if ....

		inputpwd = cleaned_data['password']
		inputrpwd = cleaned_data['rpassword']
		if inputpwd != inputrpwd :
			raise forms.ValidationError('Password not matched')

"""





"""  explicit validation

	def clean_name(self):
		inputname=self.cleaned_data['name']
		print('validating name')
		if len(inputname)<4:
			raise forms.ValidationError('the length of name field should be >= 4')
		return inputname

	def clean_rollno(self) :
		inputrollno=self.cleaned_data['rollno']
		print('validating rollno')
		return inputrollno

	def clean_email(self) :
		inputemail=self.cleaned_data['email']
		print('validating email')
		return inputemail

	def clean_feedback(self) :
		inputfeedback=self.cleaned_data['feedback']
		print('validating feedback')
		return inputfeedback
"""