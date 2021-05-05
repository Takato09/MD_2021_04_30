"""AddUser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
import AddUserApp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AddUserApp.views.UsersListView.as_view(), name='index'),
    path('edit_user/<int:pk>', AddUserApp.views.EditUserView.as_view(), name='edit_user'),
    path('add_user/', AddUserApp.views.AddUserView.as_view(), name='add_user'),
    path('get_user/<int:pk>', AddUserApp.views.GetUserView.as_view(), name='added'),
    path('delete_user/<int:pk>', AddUserApp.views.DelUserView.as_view(), name='deleted'),
]

