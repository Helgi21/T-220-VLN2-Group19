from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import DetailView
from user.forms import UserCreateForm as UsCrF
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
class UserProfile(LoginRequiredMixin, View):
    def get(self, request):
        return redirect(f'/profile/{request.user.id}')


class Profile(DetailView):
    queryset = User.objects.all()
    template_name = 'user/profile.html'

    def get_object(self, **kwargs):
        obj = super().get_object()
        return obj


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
            messages.success(request, 'Account created successfully')
            return redirect('/login/')
        else:
            messages.info(request, 'invalid registration details')
            return render(request, 'user/register.html', {
                'form': UsCrF.UserCreateForm(data=request.POST)
            })


class Login(LoginView):
    template_name = "user/login.html"
    redirect_authenticated_user = True


class Report(View):
    pass


class Pay(View):
    pass
