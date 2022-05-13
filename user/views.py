from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import DetailView, ListView, FormView
from user.forms.UserCreateForm import UserCreateForm
from user.forms.EditUserForm import EditUserForm
from user import models
from auction import models as auction_models
from user.forms.ReviewForm import ReviewForm
from django.db.models import Avg

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
            context['edit_user_form'] = EditUserForm(self.request.user.username,
                                                     data={"username": self.request.user.username,
                                                           "first_name": self.request.user.first_name,
                                                           "last_name": self.request.user.last_name,
                                                           "email": self.request.user.email,
                                                           "profile_picture": self.request.user.profile.profile_picture,
                                                           "bio": self.request.user.profile.bio,
                                                           "birthday": self.request.user.profile.birthday})
        return context

    def post(self, request, *args, **kwargs):
        if 'first_name' in request.POST:
            form = EditUserForm(self.request.user.username, data=request.POST)

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


class Register(View):
    def get(self, request):
        return render(request, 'user/register.html', {
            'form': UserCreateForm()
        })

    def post(self, request):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            profile = models.Profile()
            profile.user = User.objects.get(username=request.POST.get('username'))
            profile.save()
            messages.success(request, 'Account created successfully')
            return redirect('/login/')
        else:
            # messages.error(request, 'invalid registration details')
            return render(request, 'user/register.html', {
                'form': UserCreateForm(data=request.POST)
            })


class Login(LoginView):
    template_name = "user/login.html"
    redirect_authenticated_user = True


class Report(View):
    pass


class MyAuctions(LoginRequiredMixin, ListView):
    model = auction_models.Auction
    template_name = 'user/my_auctions.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user__id=self.request.user.id)


class Sales(LoginRequiredMixin, ListView):
    model = auction_models.Offer
    template_name = 'user/sales.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(auction__user_id=self.request.user.id).filter(status__in=[4, 5])


class Purchases(LoginRequiredMixin, ListView):
    model = auction_models.Offer
    template_name = 'user/purchases.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user_id=self.request.user.id, status__in=[4, 5])


class Review(FormView):
    template_name = 'user/review.html'
    form_class = ReviewForm
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if request.GET.get('reviewing') and request.GET.get('offer_id') and \
                self.valid_review(request.GET.get('reviewing'), request.GET.get('offer_id')):
            return super().get(request, *args, **kwargs)

        messages.error(request, "Invalid request - Contact admin if this problem persists")
        # Trick to go back and keep scroll position,
        # I could go back with HTTP_REFERER, but that would not keep scroll position
        return HttpResponse('<script>history.back();</script>')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        offer = auction_models.Offer.objects.get(id=self.request.GET.get('offer_id'))
        if self.request.GET.get('reviewing') == 'buyer':
            context['reviewed_user'] = offer.user
        else:  # reviewing seller
            context['reviewed_user'] = offer.auction.user
        context['offer_id'] = offer.id
        context['reviewing'] = self.request.GET.get('reviewing')
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            offer = auction_models.Offer.objects.get(id=self.request.GET.get('offer_id'))
            new_review = models.Review()
            new_review.description = form.cleaned_data['description']
            new_review.rating = form.cleaned_data['rating']
            new_review.offer = offer

            if self.request.GET.get('reviewing') == 'buyer':
                offer.seller_has_reviewed = True
                offer.save()

                new_review.type = 1
                new_review.reviewed_user = offer.user
                new_review.reviewer_user = offer.auction.user
                new_review.save()
                calculate_rating(offer.user)
            else:
                offer.buyer_has_reviewed = True
                offer.save()

                new_review.type = 2
                new_review.reviewed_user = offer.auction.user
                new_review.reviewer_user = offer.user
                new_review.save()
                calculate_rating(offer.auction.user)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, 'Review Sent!')
        return str(self.success_url)

    def valid_review(self, reviewing: str, offer_id: str) -> bool:
        offer = auction_models.Offer.objects.filter(id=offer_id)
        if len(offer) == 0:
            print('len failed')
            return False
        offer = offer[0]
        if reviewing == 'buyer':
            print("buyer")
            if offer.status != 5 and offer.status != 4:
                print('offer status failed')
                return False
            else:
                if offer.seller_has_reviewed:
                    print('has reviewed failed')
                    return False
            return True
        elif reviewing == 'seller':
            if offer.status != 5:
                return False
            else:
                if offer.buyer_has_reviewed:
                    return False
            return True
        else:
            return False

def calculate_rating(user):
    """
        Recalculates and updates the average rating of the user
        :param user:
    """
    reviews = models.Review.objects.filter(reviewed_user=user)
    rating = 0
    for review in reviews:
        rating += review.rating
    user.profile.rating = int(rating / len(reviews))
    user.profile.save()
