from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from . import models
from .forms.add_auction_form import AddAuctionForm, AddImageForm


# Create your views here.
class AllAuctions(View):
    def get(self, request):
        return render(request, 'user/auctions.html', {
            'auctions': models.Auction.objects.all(),
            'auction_imgs': models.Image.objects.all()
        })


class SingleAuction(View):
    def get(self, request, auction_id):
        return HttpResponse("auction with id: " + str(auction_id))


class AddAuction(View):
    def get(self, request):
        form = AddAuctionForm()
        return render(request, 'auction/add_auction.html', {
            'form': form
        })

    def post(self, request):
        form = AddAuctionForm(data=request.POST)
        if form.is_valid():
            auction = form.save()

            image = AddImageForm(data={'link': request.POST['image'], 'auction': auction.id))
            image = models.Image(image=request.POST['image'], auction=auction)
            image.save()
            tag = models.Tag(tag=request.POST['tag'], auction=auction)
            tag.save()
            return redirect('')
