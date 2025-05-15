from django.shortcuts import render
from django.http import HttpResponse

def PatientList(request):
    return HttpResponse("Details of the patients will be displayed here.")
# Create your views here.
def PatientDetail(request):
    return HttpResponse("Hi I AM presenting a patient detail page.")
