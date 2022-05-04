from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from . import models

# Create your views here.
class AllAuctions(View):
    def get(self, request):
        return render(request, 'auction/auctions.html', {
            'auctions': models.Auction.objects.all(),
            'auction_imgs': models.Image.objects.all()
        })


class SingleAuction(View):
    def get(self, request, auction_id):
        return HttpResponse("auction with id: " + str(auction_id))
