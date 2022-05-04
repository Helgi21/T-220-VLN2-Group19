from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView
from . import models
from .forms.add_auction_form import AddAuctionForm
from django.http import Http404


# Create your views here.
class AllAuctions(ListView):
    template_name = 'auction/auctions.html'
    model = models.Auction


class SingleAuction(DetailView):
    queryset = models.Auction.objects.all()
    template_name = 'auction/single_auction.html'

    def get_object(self, **kwargs):
        obj = super().get_object()
        return obj


class AddAuction(View):
    def get(self, request):
        form = AddAuctionForm()
        return render(request, 'auction/add_auction.html', {
            'form': form
        })

    def post(self, request):
        form = AddAuctionForm(data=request.POST)
        if form.is_valid():
            auction_obj = models.Auction()
            auction_obj.user = form.cleaned_data.get('user')
            auction_obj.title = form.cleaned_data['title']
            auction_obj.description = form.cleaned_data['description']
            auction_obj.price = form.cleaned_data['price']
            auction_obj.loc = form.cleaned_data.get('loc')
            auction_obj.cat = form.cleaned_data.get('cat')

            image_obj = models.Image()
            image_obj.link = form.cleaned_data['image']
            image_obj.auction = auction_obj

            auction_obj.save()
            image_obj.save()

            # TAGS DISCONTINUED FOR NOW - NOT IMPORTANT
            # for word in form.cleaned_data['tags'].split(" "):
            # tag_obj = models.Tag()
            # tag_obj.name
            # tag_obj.save()
            return redirect('/')
