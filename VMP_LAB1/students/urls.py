from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('import/', views.import_csv, name='import_csv'),
    path('import-api/', views.import_api, name='import_api'),
    path('report/', views.student_report, name='student_report'),
]