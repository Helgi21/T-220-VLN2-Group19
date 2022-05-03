from django.urls import path
from . import views

urlpatterns = [
    path('', views.Auctions.as_view(), name="auctions"),
    path('profile', views.Profile.as_view(), name="profile"),
    path('purchases', views.Purchases.as_view(), name="purchases"),
    path('sales', views.Sales.as_view(), name="sales"),
    path('register', views.Register.as_view(), name="register"),
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.Logout.as_view(), name="logout"),
    path('offers', views.Offers.as_view(), name="offers"),
    path('make_offer', views.MakeOffer.as_view(), name="offers"),
    path('report', views.Report.as_view(), name="report"),
    path('pay', views.Pay.as_view(), name="pay")
]
