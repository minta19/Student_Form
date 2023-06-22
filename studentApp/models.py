from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models import IntegerField,CharField,EmailField,PositiveIntegerField,TextField,ImageField,FileField
# Create your models here.
class Student(models.Model):
    Admission_No=IntegerField(null=False,blank=False)
    Full_Name=CharField(max_length=50,null=False,blank=False)
    Email=EmailField(max_length=100,null=False,blank=False)
    Age=PositiveIntegerField(validators=[ MaxValueValidator(17)])
    class_list=[
        ("1","1st Grade"),
        ("2","2nd Grade"),
        ("3","3rd Grade"),
        ("4","4th Grade"),
        ("5","5th Grade"),
        ("6","6th Grade"),
        ("7","7th Grade"),
        ("8","8th Grade"),
        ("9","9th Grade"),
        ("10","10th Grade"),
        ("11","11th Grade"),
        ("12","12th Grade"),
    ]
    Class=CharField(max_length=10,choices=class_list)
    Description=TextField()
    Image=ImageField(upload_to='images/')
    Marklist=FileField(upload_to='files/')

    def __str__(self) -> str:
        return self.Full_Name