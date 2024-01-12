from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse


# Create your views here.

# print('\n\n hello folks \n\n')

def home(request):
    print('\n This is View \n')
    return HttpResponse('<h1> Hello Folks </h1>')


def exception(request):
    print('\n This is exception view \n')
    x = 10/0
    return HttpResponse('This is Exception page')


def template(request):
    print('\n This is template view \n')
    context = {'name' : 'kapil'}
    return TemplateResponse(request, 'app/demo.html', context)