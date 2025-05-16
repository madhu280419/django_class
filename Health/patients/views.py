from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def PatientList(request):
    return HttpResponse("Details of the patients will be displayed here.")
# Create your views here.

def PatientDetail(request):
    return HttpResponse("Hi I AM presenting a patient detail page.")

def patients(request):
    template = loader.get_template('patients.html')
    return HttpResponse(template.render())
    
