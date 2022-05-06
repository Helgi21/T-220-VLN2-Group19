from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllAuctions.as_view(), name="auctions"),
    path('<int:pk>/', views.SingleAuction.as_view(), name="single_auction"),
    path('add_auction/', views.AddAuction.as_view(), name="add_auction"),
    path('offers/', views.ViewOffers.as_view(), name="offers"),
]
