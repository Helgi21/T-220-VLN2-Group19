from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView
from . import models
from .forms.add_auction_form import AddAuctionForm
from .forms.make_offer_form import MakeOfferForm
from .forms.make_counter_offer_form import MakeCounterOfferForm
from django.contrib import messages

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

    def get_context_data(self, **kwargs):
        form = MakeOfferForm()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context

    def post(self, request, pk):
        form = MakeOfferForm(data=request.POST)
        if form.is_valid():
            offer_obj = models.Offer()
            offer_obj.price = form.cleaned_data.get('price')
            offer_obj.auction = models.Auction.objects.get(id=pk)
            offer_obj.user = request.user
            offer_obj.status = 1
            offer_obj.save()

            messages.success(request, 'Offer sent!')

            return redirect(f'/{pk}/')


class AddAuction(LoginRequiredMixin, View):
    def get(self, request):
        form = AddAuctionForm()
        return render(request, 'auction/add_auction.html', {
            'form': form
        })

    def post(self, request):
        form = AddAuctionForm(data=request.POST)
        if form.is_valid():
            auction_obj = models.Auction()
            auction_obj.user = request.user
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


class ViewOffers(LoginRequiredMixin, ListView):
    template_name = 'auction/offers.html'
    # paginate_by = 100
    model = models.Offer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user).exclude(status=5).exclude(status=2)

    def get_context_data(self, *args):
        context = super().get_context_data()
        context['received_offers'] = models.Offer.objects.all().filter(auction__user=self.request.user) \
            .exclude(status__in=[5, 2])
        q2 = models.Offer.objects.all().filter(user=self.request.user).filter(status=2)

        context['received_offers'] = context['received_offers'].union(q2)
        return context

    def post(self, request):
        if 'counter_offer_id' in request.POST:  # Counter offer only
            print("in if")
            offer_id = request.POST['counter_offer_id']
            print(offer_id)
            offer_price = request.POST['counter_offer_price']

            offer = models.Offer.objects.get(id=offer_id)

            offer.price = offer_price
            offer.status = 2
            print(offer.auction.title)

            offer.save()
            messages.success(request, f'Counter offer sent!')

            return redirect(f'/offers/?received_offers')

        else:  # Accept or decline only
            offer_response = request.POST['offer_response'].split('_')

            offer = models.Offer.objects.get(id=offer_response[1])
            offer.status = offer_response[0]

            offer.save()

            if offer_response == 5:
                messages.success(request, f'Offer accepted!')
            elif offer_response == 4:
                messages.success(request, f'Offer declined!')

            return redirect(f'/offers/?received_offers')



