from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from . import models


# Create your views here.
class Profile(View):
    def get(self, request, profile_id):
        return HttpResponse("this is the profile view of user with id" + str(profile_id))


class Purchases(View):
    pass


class Sales(View):
    pass


class Register(View):
    pass


class Login(View):
    pass


class Logout(View):
    pass


class Report(View):
    pass


class Pay(View):
    pass
