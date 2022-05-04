from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllAuctions.as_view(), name="auctions"),
    path('<int:auction_id>', views.SingleAuction.as_view(), name="single_auction")
]
