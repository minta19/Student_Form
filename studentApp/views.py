from django.shortcuts import render,redirect
from .forms import StudentCreate
from .models import Student
from django.views.generic import ListView
# Create your views here.

def CreateStudent(request):
    form=StudentCreate()
    if request.method == 'POST':
        form=StudentCreate(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('createstudent')
    context={"form":form}
    return render(request,'studentApp/studtemp.html',context) 

class StudentView(ListView):
    template_name = 'studentApp/stuview.html'
    queryset=Student.objects.all()
    context_object_name="allstudent"

