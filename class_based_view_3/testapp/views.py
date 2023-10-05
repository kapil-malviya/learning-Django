from django.shortcuts import render
from .models import Company
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.



class CompanyListView(ListView):
	model = Company 
	# default template file : company_list.html
	# default context object : company_list



class CompanyDetailView(DetailView):
	model = Company 
	# default template file : company_detail.html
	# default context object : company 



class CompanyCreateView(CreateView):
	model = Company 
	# whenever defining createview, we must provide fields attributes
	fields = ('name', 'location', 'ceo')
	# default template file : company_form.html



class CompanyUpdateView(UpdateView):
	model = Company 
	fields = ('name', 'location', 'ceo') # fields allowed to update
	# internally it will use company_form.html template file, we don't need to create template file specifically for this



class CompanyDeleteView(DeleteView):
	model = Company 
	success_url = reverse_lazy('companies')     # success_url = predefined word related to the delete view
	# default template file : company_confirm_delete.html