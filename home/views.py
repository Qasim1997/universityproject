from django.contrib import messages
from django.db.models import Q
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
import stripe
stripe.api_key = "sk_test_26PHem9AhJZvU623DfE1x4sd"


# from home.models import Customer
from home.models import City, Hotel, Cart, UserDetail
from .forms import CustomerRegistrationForm, EditChangeForm, DetailForm


def dumy(request):
    region = City.get_all_city()
 #   print("hello", region)
    return render(request, 'html/base.html', {'region': region})


def home(request):
    hotel = None
    region = City.get_all_city()
    cityID = request.GET.get('city')
    if cityID:
        hotel = Hotel.get_all_hotel_by_city_id(cityID)
    else:
        hotel = Hotel.get_all_hotel()

    return render(request, 'html/home.html', {'hotels': hotel, 'region': region})


class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'html/signup.html', {'form': form})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')

        return render(request, 'html/signup.html', {'form': form})


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditChangeForm(request.POST, instance=request.user)
            if fm.is_valid():
                messages.success(request, 'Profile updated !!')
                fm.save()
        else:
            fm = EditChangeForm(instance=request.user)
        return render(request, 'html/profile.html', {'name': request.user, 'form': fm})
    else:
        return HttpResponseRedirect('/login')


class HotelDetailView(View):
    def get(self, request, pk):
        hotel = Hotel.objects.get(pk=pk)
        region = City.get_all_city()

     #   hotel_detail = HotelDetail.objects.filter()
        return render(request, 'html/detail.html', {'hotel': hotel, 'region': region})

def add_to_cart(request):
    user = request.user
    hotel_id = request.GET.get('prod_id')
    print(hotel_id)
    hotel = Hotel.objects.get(id=hotel_id)
    Cart(user=user, hotel=hotel).save()
    return redirect('/cart')
    # return render(request, 'html/checks.html')



def show_cart(request):
    if request.user.is_authenticated:
        region = City.get_all_city()
        #prod_id = request.GET['prod_id']
        hotel_id = request.GET.get('prod_id')
        user = request.user
        #cart = Cart.objects.all()
        cart = Cart.objects.filter(Q(user=request.user) )
     
        amount = 0.0
        services_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity *p.hotel.price)
                amount += tempamount
                totalamount = amount + services_amount
            return render(request, 'html/addtocart.html',{'amount': amount,'carts': cart, 'totalamount': totalamount ,'region': region})
        else:
            return render(request, 'html/emptycart.html')



def plus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        # data = Cart.objects.filter(Q(user=request.user) & Q(hotel=prod_id))
        # print('..................',data)
        print(prod_id)
        c = Cart.objects.get(Q(hotel=prod_id) & Q(user=request.user))
        # c = Cart.objects.get(Q(hotel=prod_id) & Q(user=request.user)  )
        print("Cart....................... CArt qasim ,sfsd,f;lsd,fsd;f,.;'.ff;sd'f.sdf;' ")
        print('c',c)
        c.quantity +=1
        c.save()
        amount = 0.0
        services_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
        print( 'cart', cart_product)
        # if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.hotel.price)
            amount += tempamount
                

        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount': amount + services_amount
        }
        print('data',data)
        return  JsonResponse(data)

def minus_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        print('id',prod_id)
        c = Cart.objects.get(Q(user=request.user) &Q(hotel=prod_id))
        print('c',c)
        c.quantity -=1
        c.save()
        amount = 0.0
        services_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
        print( 'cart', cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.hotel.price)
                amount += tempamount
            

            data = {
                'quantity' : c.quantity,
                'amount' : amount,
                'totalamount': amount + services_amount
            }
            print('data',data)
            return  JsonResponse(data)


def remove_cart(request):
    if request.method == "GET":
        prod_id = request.GET['prod_id']
        print('id',prod_id)
        c = Cart.objects.get(Q(user=request.user) &Q(hotel=prod_id))
        print('c',c)
        c.delete()
        amount = 0.0
        services_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user ==request.user]
        print( 'cart', cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.hotel.price)
                amount += tempamount
            data = {
                'amount' : amount,
                'totalamount': amount + services_amount
            }
            print('data',data)
            return  JsonResponse(data)
def search(request):
    query = request.GET['query']
    region = City.get_all_city()
    allhotel = Hotel.objects.filter(title__icontains=query)
    params = {'hotels': allhotel, 'disco': region}
    return render(request, 'html/search.html', params)
