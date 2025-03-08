"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from expense import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup_page, name='signup_page'),
    path('home/', views.home_page, name='home_page'),
    path('delete_entry/<int:pk>', views.deleteEntry, name='delete_entry'),
    path('profile/', views.profile_page, name='profile_page'),
    path('analysis/', views.analysis_page, name='analysis_page'),
    path('logout/', views.logout_page, name='logout_page')
]
