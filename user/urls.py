from django.urls import path
from . import views

urlpatterns = [
    path('', views.auctions, name="auctions"),
    path('/profile', views.profile, name="profile"),
    path('/purchases', views.purchases, name="purchases"),
    path('/sales', views.sales, name="sales"),
    path('/register', views.register, name="register"),
    path('/login', views.login, name="login"),
    path('/logout', views.logout, name="logout"),
    path('/offers', views.offers, name="offers"),
    path('/make_offer', views.make_offer, name="offers"),
    path('/report', views.report, name="report"),
    path('/pay', views.pay, name="pay")
]