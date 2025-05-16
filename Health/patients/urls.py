from django.urls import path
from patients.views import PatientList, PatientDetail,patients
urlpatterns = [
    path('patients/', PatientList, name='patient-list'),
    path('PatientDetail/', PatientDetail , name='patientDetail'),
    path('patient/', patients, name='patients')
]
