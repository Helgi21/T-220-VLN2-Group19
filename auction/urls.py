from django.urls import path
from . import views

app_name = "auction"

urlpatterns = [
    path('', views.AllAuctions.as_view(), name="auctions"),
    path('<int:pk>/', views.SingleAuction.as_view(), name="singleAuction"),
    path('add_auction/', views.AddAuction.as_view(), name="addAuction"),
    path('offers/', views.ViewOffers.as_view(), name="offers"),
    path('pay/<int:id>', views.Pay.as_view(), name="pay")
]
