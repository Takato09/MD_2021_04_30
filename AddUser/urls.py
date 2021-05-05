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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AddUserApp.views.UserListView.as_view(), name='index'),
    path('edit_user/<int:pk>', AddUserApp.views.UserEditView.as_view(), name='edit_user'),
    path('add_user/', AddUserApp.views.RegisterView.as_view(), name='add_user'),
    path('get_user/<int:pk>', AddUserApp.views.UserDetailView.as_view(), name='added'),
    path('delete_user/<int:user_id>', AddUserApp.views.delete_user),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

