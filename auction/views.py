from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView
from django.db.models import Q
from . import models
from user import models as user_models
from .forms.add_auction_form import AddAuctionForm
from .forms.make_offer_form import MakeOfferForm
from .forms.pay_forms import ContactPayForm, PaymentPayForm
from .forms.make_counter_offer_form import MakeCounterOfferForm
from django.contrib import messages
from user.notifications import Notification
from django.db.models import Avg

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
        old = self.request.GET.get('old')
        if search and order_by and direction and category and old:
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
                a = models.Auction.objects.filter(title__icontains=search).filter(is_finished=old)
                a = a.union(models.Auction.objects.filter(description__icontains=search).filter(is_finished=old))
            else:
                a = models.Auction.objects.filter(title__icontains=search, cat_id=category).filter(is_finished=old)
                a = a.union(models.Auction.objects
                            .filter(description__icontains=search, cat_id=category).filter(is_finished=old))

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
        context['highest_offer'] = models.Offer.objects.filter(auction=self.object).order_by('-price').first()
        accepted_paid = models.Offer.objects.filter(auction=self.object, status__in=[4, 5])
        all_similar_items = models.Auction.objects.filter(cat=self.object.cat, is_finished=False).exclude(id=self.object.id)

        if len(accepted_paid) > 0:
            print("acc off")
            context['accepted_offer'] = accepted_paid[0]

        similar_items = []
        for i, x in enumerate(all_similar_items):
            if i >= 4:
                break
            similar_items.append(x)

        if len(similar_items) > 0:
            context['similar_items'] = similar_items

        return context

    def post(self, request, pk):
        print(request.POST)
        if 'delete_auction' in request.POST:
            auction_id = request.POST['delete_auction']
            auction = models.Auction.objects.get(id=pk)
            if auction.is_finished:
                messages.error(request, 'Cannot delete this auction')
                return redirect('/')

            auction.delete()
            messages.success(request, 'Auction deleted!')
            return redirect('/')

        form = MakeOfferForm(data=request.POST)
        if form.is_valid():
            auction = models.Auction.objects.get(id=pk)
            offer_obj = models.Offer()
            offer_obj.price = form.cleaned_data.get('price')
            offer_obj.auction = auction
            offer_obj.user = request.user
            offer_obj.status = 1
            offer_obj.save()

            messages.success(request, 'Offer sent!')
            # TODO: in notification link filter by auction when/if /offer supports it
            Notification("New Offer!",
                         str(f"You have received a new offer from user '{request.user.username}'"
                             f" on your item '{models.Auction.objects.get(id=pk).title}'. "
                             f"Offered price: {form.cleaned_data.get('price')}"),
                         auction.user,
                         "/offers/?received_offers")

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

            auction_obj.save()

            image_list = form.cleaned_data['image'].split()

            for image in image_list:
                image_obj = models.Image()
                image_obj.link = image
                image_obj.auction = auction_obj

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
        return qs.filter(user=self.request.user).exclude(status=5).exclude(status=2).order_by('-creation_time')

    def get_context_data(self, *args):
        context = super().get_context_data()
        context['received_offers'] = models.Offer.objects.all().filter(auction__user=self.request.user) \
            .exclude(status__in=[5, 2])
        q2 = models.Offer.objects.all().filter(user=self.request.user).filter(status=2)

        context['received_offers'] = context['received_offers'].union(q2).order_by('-creation_time')
        return context

    def post(self, request):
        if 'counter_offer_id' in request.POST:  # Counter offer only
            offer_id = request.POST['counter_offer_id']
            offer_price = request.POST['counter_offer_price']

            offer = models.Offer.objects.get(id=offer_id)
            old_offer_price = offer.price

            offer.price = offer_price
            offer.status = 2
            print(offer.auction.title)

            offer.save()
            Notification("Counter Offer!",
                         str(f"You have received a counter offer on the item '{offer.auction.title}'. "
                             f"Your offered price: {old_offer_price}kr. "
                             f"Their counter offer: {offer.price}kr. "),
                         offer.user,
                         "/offers/?received_offers")
            messages.success(request, 'Counter offer sent!')

            return redirect(f'/offers/?received_offers')

        elif 'cancel_offer' in request.POST:  # Cancel offers
            offer_id = request.POST['cancel_offer']
            offer = models.Offer.objects.get(id=offer_id)
            if offer.status == 4 or offer.status == 5:
                messages.error(request, 'Cannot cancel this offer')
                return redirect(f'/offers')

            offer.delete()
            messages.success(request, 'Offer cancelled!')
            return redirect(f'/offers')

        else:  # Accept or decline only
            offer_response = request.POST['offer_response'].split('_')

            offer = models.Offer.objects.get(id=offer_response[1])
            offer.status = offer_response[0]
            offer.is_finished = True

            offer.save()
            if offer_response[0] == str(4):
                print(offer_response[0])
                offers_to_update = Offer.objects.all()
                for offer_to_decline in offers_to_update:
                    if offer_to_decline.id != int(offer_response[1]) and offer_to_decline.auction.id == offer.auction.id:
                        Notification("Offer Declined", str(f"Your offer of {offer_to_decline.price}Kr "
                                                           f"on item '{offer.auction.title}' has been declined."),
                                     offer.user, "/offers/")
                        offer_to_decline.status = 3
                        offer_to_decline.save()
            print(offer.status)
            if offer.status == str(4):
                print("accepted")
                Notification("Offer Accepted!", str(f"Your offer of {offer.price}Kr on item '{offer.auction.title}' "
                                                    f"has been accepted! Please proceed to pay for the product."),
                             offer.user, "/offers/")
                messages.success(request, f'Offer accepted!')

            elif offer.status == str(3):
                print("declined")
                Notification("Offer Declined", str(f"Your offer of {offer.price}Kr "
                                                   f"on item '{offer.auction.title}' has been declined."),
                             offer.user, "/offers/")
                messages.success(request, f'Offer declined!')

            return redirect(f'/offers/?received_offers')


class Pay(LoginRequiredMixin, DetailView):
    model = Offer
    template_name = 'auction/pay.html'
    success_url = '/purchases/'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.GET.get('fill_in_saved') != None and request.GET.get('fill_in_saved') != 'dont_use_saved':
            data = user_models.CardInfo.objects.get(id=request.GET.get('fill_in_saved'))
            self.contact_form = ContactPayForm(initial={
                'first_name': data.first_name,
                'last_name': data.last_name,
                'street_name': data.street,
                'house_number': data.house_number,
                'city': data.city,
                'country': data.country,
                'zip': data.zip
            }, prefix="contact_form")
            self.payment_form = PaymentPayForm(initial={
                'cardholder_first_name': data.cardholder_first_name,
                'cardholder_last_name': data.cardholder_last_name,
                'card_number': data.card_number,
                'expires': data.expires,
                'cvc': data.cvc
            }, prefix="payment_form")
        else:
            self.contact_form = ContactPayForm(initial={'first_name': request.user.first_name,
                                                    'last_name': request.user.last_name}, prefix='contact_form')
            self.payment_form = PaymentPayForm(initial={'cardholder_first_name': request.user.first_name,
                                                    'cardholder_first_name': request.user.last_name}, prefix='payment_form')
        pk = self.object.id
        if request.user.id != self.object.user.id or (self.object.status != 4 and self.object.status != 5):
            messages.error(request, "Invalid request - Contact admin if this problem persists")
            # Trick to go back and keep scroll position,
            # I could go back with HTTP_REFERER, but that would not keep scroll position
            return HttpResponse('<script>history.back();</script>')

        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'contact_pay_form' in kwargs and 'contact_pay_form' in kwargs:
            context['contact_form'] = ContactPayForm(self.request.POST, prefix='contact_form')
            context['payment_form'] = PaymentPayForm(self.request.POST, prefix='payment_form')
        else:
            context['contact_form'] = self.contact_form
            context['payment_form'] = self.payment_form
        return context

    def post(self, request, pk):
        self.object = models.Offer.objects.get(id=pk)
        print(request.POST)
        contact_form = ContactPayForm(request.POST, prefix='contact_form')
        payment_form = PaymentPayForm(request.POST, prefix='payment_form')
        if contact_form.is_valid() and payment_form.is_valid():
            if request.POST.get('payment_detail_save-checkbox') == 'on':
                cardinfo_instance = user_models.CardInfo()
                cardinfo_instance.first_name = contact_form.cleaned_data['first_name']
                cardinfo_instance.last_name = contact_form.cleaned_data['last_name']
                cardinfo_instance.card_number = payment_form.cleaned_data['card_number']
                cardinfo_instance.cvc = payment_form.cleaned_data['cvc']
                cardinfo_instance.expires = payment_form.cleaned_data['expires']
                cardinfo_instance.street = contact_form.cleaned_data['street_name']
                cardinfo_instance.city = contact_form.cleaned_data['city']
                cardinfo_instance.zip = contact_form.cleaned_data['zip']
                cardinfo_instance.country = user_models.Country.objects.get(id=contact_form.cleaned_data['country'].id)
                cardinfo_instance.user = request.user
                cardinfo_instance.house_number = contact_form.cleaned_data['house_number']
                cardinfo_instance.cardholder_first_name = payment_form.cleaned_data['cardholder_first_name']
                cardinfo_instance.cardholder_last_name = payment_form.cleaned_data['cardholder_last_name']

                cardinfo_instance.save()
            offer_instance = Offer.objects.get(id=pk)
            offer_instance.status = 5
            offer_instance.save()
            messages.success(request, "Payment successful!")
            return self.forms_valid(contact_form, payment_form)
        else:
            print("pay fail")
            return self.forms_invalid(contact_form, payment_form)

    def forms_valid(self, form1, form2):
        """If the form is valid, redirect to the supplied URL."""
        return HttpResponseRedirect(self.success_url)

    def forms_invalid(self, form1, form2):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(contact_pay_form=form1, payment_pay_form=form2))
