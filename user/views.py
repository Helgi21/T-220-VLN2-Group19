from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
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
    def get(self, request):
        return render(request, 'user/register.html', {
            'form': UserCreationForm()
        })

    def post(self, request):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
        else:
            return HttpResponse("failed")

class Report(View):
    pass


class Pay(View):
    pass
