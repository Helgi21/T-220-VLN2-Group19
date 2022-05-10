from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import DetailView
from user.forms import UserCreateForm as UsCrF
from user.forms import EditUserForm as EdUsF
from django.contrib.auth import get_user_model
from user import models
User = get_user_model()


# Create your views here.
class UserProfile(LoginRequiredMixin, View):
    def get(self, request):
        return redirect(f'/profile/{request.user.id}')


class Profile(LoginRequiredMixin, DetailView):
    queryset = User.objects.all()
    template_name = 'user/profile.html'

    def get_object(self, **kwargs):
        obj = super().get_object()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['payment_options'] = None
        context['edit_user_form'] = None
        if self.request.user == self.object:
            context['payment_options'] = self.object.cards
            context['edit_user_form'] = EdUsF.EditUserForm(self.request.user.username,
                                                           data={"username": self.request.user.username,
                                                                 "first_name": self.request.user.first_name,
                                                                 "last_name": self.request.user.last_name,
                                                                 "email": self.request.user.email,
                                                                 "profile_picture":
                                                                     self.request.user.profile.profile_picture,
                                                                 "bio": self.request.user.profile.bio,
                                                                 "birthday": self.request.user.profile.birthday})
        return context

    def post(self, request, *args, **kwargs):
        if 'first_name' in request.POST:
            form = EdUsF.EditUserForm(self.request.user.username, data=request.POST)

            if form.is_valid():
                user_model_instance = User.objects.get(id=request.user.id)
                user_model_instance.first_name = form.cleaned_data['first_name']
                user_model_instance.last_name = form.cleaned_data['last_name']
                user_model_instance.email = form.cleaned_data['email']
                user_model_instance.profile.bio = form.cleaned_data['bio']
                user_model_instance.profile.profile_picture = form.cleaned_data['profile_picture']
                user_model_instance.profile.birthday = form.cleaned_data['birthday']
                user_model_instance.save()
                user_model_instance.profile.save()
                messages.success(request, 'Profile Successfully Updated')
                return redirect(f"/profile/{request.user.id}?profile_info")
            else:
                for error in form.errors:
                    print(error)
                messages.error(request, form.errors, extra_tags='edit_form_msg_li')
                return redirect(f"/profile/{request.user.id}?profile_edit")

        else:
            print("payment post request")


class Purchases(LoginRequiredMixin, View):
    pass


class Sales(LoginRequiredMixin, View):
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
            print(request.POST)
            profile = models.Profile()
            profile.user = User.objects.get(username=request.POST.get('username'))
            profile.save()
            messages.success(request, 'Account created successfully')
            return redirect('/login/')
        else:
            messages.error(request, 'invalid registration details')
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
