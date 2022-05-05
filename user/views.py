from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from user.forms import UserCreateForm as UsCrF


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
            'form': UsCrF.UserCreateForm()
        })

    def post(self, request):
        form = UsCrF.UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
        else:
            return HttpResponse("failed")


class Report(View):
    pass


class Pay(View):
    pass
