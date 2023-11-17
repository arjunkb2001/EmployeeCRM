from django.shortcuts import render,redirect
from django.views.generic import View
from crm.forms import *
from crm.models import Employee
from django.contrib import messages

from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout

from django.utils.decorators import method_decorator

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"invalid session")
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper


# Create your views here.

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")


class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")
    def post(self,request,*args,**kwargs):
        name=request.POST.get("boxs")
        qs=Employee.objects.filter(name__icontains=name)
        return render(request,"emplist.html",{"data":qs})

@method_decorator(signin_required,name="dispatch")
class EmployeCreateView(View):
    
    def get(self,request,*args,**kwargs):
        form=EmployeModelForm()
        return render(request,"emp_add.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=EmployeModelForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee has been created")
            # Employee.objects.create(**form.cleaned_data)
            print("created")
            return render(request,"emp_add.html",{"form":form})
        else:
            messages.error(request,"Failed To Add Employee")
            return render(request,"emp_add.html",{"form":form})


@method_decorator(signin_required,name="dispatch")
class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        department=Employee.objects.all().values_list("department",flat=True).distinct()
        print(department)
        if "department"  in request.GET:
            dept=request.GET.get("department")
            qs=qs.filter(department__iexact=dept)
        return render(request,"emplist.html",{"data":qs,"department":department})
        
    def post(self,request,*args,**kwargs):
        name=request.POST.get("boxs")
        qs=Employee.objects.filter(name__icontains=name)
        return render(request,"emplist.html",{"data":qs})



@method_decorator(signin_required,name="dispatch")
class EmployeDetailView(View):
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        return render(request,"empdetials.html",{"data":qs})

@method_decorator(signin_required,name="dispatch")
class EmpDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employee.objects.get(id=id).delete()
        messages.success(request,"Employee Is Removed")
        return redirect("emplist")


@method_decorator(signin_required,name="dispatch")
class EmpUpdateView(View):
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        obj=Employee.objects.get(id=id)
        form=EmployeModelForm(instance=obj)
        return render(request,"emp_edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Employee.objects.get(id=id)
        form=EmployeModelForm(request.POST,files=request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request,"Employee Updated")
            # Employee.objects.create(**form.cleaned_data)
            print("created")
            return redirect("empdetail",pk=id)
        else:
            messages.error(request,"Failed To Updated")
            return render(request,"emp_add.html",{"form":form})
        
        # localhost:8000/signup/
        
class SiginupView(View):
    def get(self,request,*args, **kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args, **kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"created")
            return render(request,"register.html",{"form":form})
        else:
            messages.error(request,"failed")
            return render(request,"register.html",{"form":form})
    
class SignInView(View):
    def get(self,request,*args, **kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args, **kwargs):
        form=LoginForm(request.POST)
       
        if form.is_valid():
            user_name=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password')
            print(user_name,pwd)
            user_obj=authenticate(request,username=user_name,password=pwd)
            print(user_obj)
            if user_obj:
                print(user_obj)
                print("valid credintial")
                login(request,user_obj)
            
            return redirect("home")
            
        else:

            return render(request,'login.html',{"form":form})


@method_decorator(signin_required,name="dispatch")
class SignOutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return redirect("login")