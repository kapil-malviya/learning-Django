from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse

# Create your views here.

class HelloKapil(View):
	def get(self, request):
		return HttpResponse('<h1> this is from class based views </h1>')



class TemplateView(TemplateView):
	template_name = 'testapp/result.html'



class HelloTemplateContext(TemplateView):
	template_name = 'testapp/info.html'

	def get_context_data(self, **kwrgs):
		context = super().get_context_data(**kwrgs)
		context['name'] = 'kapil'
		context['subject'] = 'DRF'
		context['marks'] = 88
		return context