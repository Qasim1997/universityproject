from django.urls import path
from home import views
from django.contrib.auth import  views as auth_views
from .forms import LoginForm
urlpatterns = [
    path('', views.home, name="home"),
    path('dumy', views.dumy,name='dumy'),
    path('signup', views.CustomerRegistrationView.as_view(),name='registration'),
    path('login',auth_views.LoginView.as_view(
    template_name='html/login.html', authentication_form=LoginForm), name='login'),
    path('logout',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('hotel-detail/<int:pk>', views.HotelDetailView.as_view(), name='hotel-detail'),
    path('add-to-cart', views.add_to_cart, name='add to cart'),
    path('cart', views.show_cart, name='cart'),
    path('pluscart', views.plus_cart),
    path('minuscart', views.minus_cart),
    path('removecart', views.remove_cart),
    path('search', views.search, name="query"),
]