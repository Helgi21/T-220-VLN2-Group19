from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from . import models


# Create your views here.
class Profile(View):
    def get(self, request):
        return HttpResponse("this is the profile view")


class Auctions(View):
    def get(self, request):
        data = models.Auction.objects.all()
        return render(request, 'user/auctions.html', data)


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


class Offers(View):
    pass


class MakeOffer(View):
    pass


class Report(View):
    pass


class Pay(View):
    pass