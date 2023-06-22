from django.urls import path
from .import views
urlpatterns=[
    path('create/',views.CreateStudent,name="createstudent")
]