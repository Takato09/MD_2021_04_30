from django.views.generic import (
    ListView,
    View,
    )
from django.shortcuts import render
from AddUserApp import models


class AddUserView(View):

    def get(self, request):

        return render(
            template_name='AddUser/form.html',
            request=request,
        )

    def post(self, request):

        adduser = models.Adduser(
            username=request.POST['username'],
            email=request.POST['email'],
        )
        adduser.save()

        context = {
            'username': adduser.username,
            'email': adduser.email,
        }

        return render(
            template_name='AddUser/added.html',
            request=request,
            context=context,
        )


class DelUserView(View):

    def get(self, request):
        added_users = models.Adduser.objects.all()
        for user in added_users:
            if user.id == user_id:
                context = {
                    'username': user.username,
                }
                user.delete()

        return render(
            request=request,
            template_name='AddUser/delete.html',
            context=context,
        )


class EditUserView(View):

    def get(self, request):
        return render(
            template_name='AddUser/edit_form.html',
            request=request,
            context=context,
        )

    def post(self, request):
        adduser = models.Adduser(
            id=user_id,
            username=request.POST['username'],
            email=request.POST['email'],
        )

        adduser.save()

        context = {
            'username': adduser.username,
            'email': adduser.email,
        }

        return render(
            template_name='AddUser/added.html',
            request=request,
            context=context,
        )

    added_users = models.Adduser.objects.all()
    for user in added_users:
        if user.id == user_id:
            context = {
                'username': user.username,
                'email': user.email,
            }


class GetUserView(View):
    def get(self, request):
        added_users = models.Adduser.objects.all()
        for user in added_users:
            if user.id == pk:
                context = {
                    'username': user.username,
                    'email': user.email,
                }
        return render(
            template_name='AddUser/added.html',
            request=request,
            context=context,
        )


class UsersListView(ListView):
    template_name = 'AddUser/index.html'
    model = models.Adduser.objects.all()

