from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    # Spath('', views.Auctions.as_view(), name="auctions"),
    path('profile/<int:profile_id>', views.Profile.as_view(), name="profile"),
    path('purchases/', views.Purchases.as_view(), name="purchases"),
    path('sales/', views.Sales.as_view(), name="sales"),
    path('register/', views.Register.as_view(), name="register"),
    path('login/', LoginView.as_view(template_name="user/login.html"), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name="logout"),
    path('report/', views.Report.as_view(), name="report"),
    path('pay/', views.Pay.as_view(), name="pay")
]
