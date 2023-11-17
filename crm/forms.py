from django import forms

from crm.models import *

from django.contrib.auth.models import User



class EmployeModelForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

        widgets={
            'name':forms.TextInput(attrs={"class":"form-control",'placeholder':"enter your name"}),
            'department':forms.TextInput(attrs={"class":"form-control",'placeholder':"enter your department"}),
            'salary':forms.NumberInput(attrs={"class":"form-control",'placeholder':"enter your "}),
            'email':forms.TextInput(attrs={"class":"form-control"}),
            'age':forms.NumberInput(attrs={"class":"form-control"}),
            'contact':forms.TextInput(attrs={"class":"form-control"}),
            'dob':forms.DateInput(attrs={"class":"form-control","type":"date"})
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"enter your username"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"enter your email"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"enter your password"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))