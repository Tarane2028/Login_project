"""hello_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from HelloWorld_App import views
from HelloWorld_App.forms import LoginForm
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm



urlpatterns = [
    
    path("", views.sayHello),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(),name='category'),
    path("category-title/<val>", views.CategoryTitle.as_view(),name='category-title'),
    path("product-detail/<int:pk>", views.ProductDetail.as_view(),name='product-detail'),

    #login authentication
    path('registraion/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm) , name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
