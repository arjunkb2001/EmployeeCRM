"""
URL configuration for employeecrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crm import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexView.as_view(),name="index"),
    path('employee/home',views.HomeView.as_view(),name="home"),
    path('employee/add',views.EmployeCreateView.as_view(),name="emp-add"),
    path('employee/all',views.EmployeeListView.as_view(),name="emplist"),
    path("employee/<int:pk>",views.EmployeDetailView.as_view(),name="empdetail"),
    path('employee/<int:pk>/remove',views.EmpDeleteView.as_view(),name="deleteemp"),
    path('employee/<int:pk>/change',views.EmpUpdateView.as_view(),name="updateemp"),
    path('employee/reg/',views.SiginupView.as_view(),name="reg"),
    path('employee/login/',views.SignInView.as_view(),name="login"),
    path('employee/logout',views.SignOutView.as_view(),name="signout")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)