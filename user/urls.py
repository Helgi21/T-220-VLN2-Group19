from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('profile/', views.UserProfile.as_view(), name="user_profile"),
    path('profile/<int:pk>/', views.Profile.as_view(), name="profile"),
    path('purchases/', views.Purchases.as_view(), name="purchases"),
    path('sales/', views.Sales.as_view(), name="sales"),
    path('my_auctions/', views.MyAuctions.as_view(), name="myAuctions"),
    path('register/', views.Register.as_view(), name="register"),
    path('login/', views.Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('report/', views.Report.as_view(), name="report"),
    path('review/', views.Review.as_view(), name="review")
]
