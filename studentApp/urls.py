from django.urls import path
from .import views
from .views import StudentView
urlpatterns=[
    path('create/',views.CreateStudent,name="createstudent"),
    path('studview/',views.StudentView.as_view(),name='stud_list')
]