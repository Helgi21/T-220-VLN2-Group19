from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
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
from .models import Offer


class AllAuctions(ListView):
    template_name = 'auction/auctions.html'
    model = models.Auction

    def get(self, *args, **kwargs):
        search = self.request.GET.get('search')
        order_by = self.request.GET.get('order_by')
        direction = self.request.GET.get('direction')
        category = self.request.GET.get('category')
        if search and order_by and direction and category:
            if search == "*":
                search = ""

            dir_map = {
                'asc': '',
                'desc': '-'
            }
            if order_by == 'price' or order_by == 'title':
                dir_map['asc'] = '-'
                dir_map['desc'] = ''

            direction = dir_map[direction]

            if category == 'all':
                a = models.Auction.objects.filter(title__icontains=search).exclude(offer__status__in=[4, 5])
                a = a.union(models.Auction.objects.filter(description__icontains=search).exclude(offer__status__in=[4, 5]))
            else:
                a = models.Auction.objects.filter(title__icontains=search, cat_id=category).exclude(offer__status__in=[4, 5])
                a = a.union(models.Auction.objects.filter(description__icontains=search, cat_id=category).exclude(offer__status__in=[4, 5]))
            print(a)
            a = a.order_by(str(direction) + str(order_by))
            auctions = [{
                'id': x.id,
                'title': x.title,
                'price': x.price,
                'cat': x.cat.id,
                'loc': x.loc.id,
                'user': x.user.id,
                'first_pic': x.images.first().link,
                'creation_time': x.creation_time
            } for x in a]
            return JsonResponse({"data": auctions})
        else:
            # ignore this warning
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            return self.render_to_response(context)

    def get_queryset(self):
        qs = self.model.objects.exclude(offer__status__in=[4, 5]).order_by('-creation_time')
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['categories'] = models.Category.objects.all()
        return context


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
            auction_obj.condition = form.cleaned_data.get('condition')

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
            offer_id = request.POST['counter_offer_id']
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
            if offer_response[0] == str(4):
                print(offer_response[0])
                offers_to_update = Offer.objects.all()
                for offer_to_decline in offers_to_update:
                    print(offer_to_decline)
                    if offer_to_decline.id != int(offer_response[1]) and offer_to_decline.auction.id == offer.auction.id:
                        offer_to_decline.status = 3
                        offer_to_decline.save()

            if offer_response == 5:
                messages.success(request, f'Offer accepted!')
            elif offer_response == 4:
                messages.success(request, f'Offer declined!')

            return redirect(f'/offers/?received_offers')


class Pay(LoginRequiredMixin, DetailView):
    model = Offer
    template_name = 'auction/pay.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['auction'] = self.object.auction
        return context

    def post(self, request, pk):
        offer_instance = Offer.objects.get(id=pk)
        offer_instance.status = 5
        offer_instance.save()

        # offers_to_update = Offer.objects.all()
        # for offer in offers_to_update:
        #     if offer.id != pk and offer.auction == offer_instance.auction:
        #         offer.status = 3
        #         offer.save()



        messages.success(request, f'Payment sent!')
        return redirect(f'/offers')
