from django.urls import path
from patients.views import PatientList, PatientDetail
urlpatterns = [
    path('patients/', PatientList, name='patient-list'),
    path('PatientDetail/', PatientDetail , name='patientDetail')
]
