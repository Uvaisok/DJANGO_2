from django.shortcuts import render,redirect
from . models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from . models import Order,OrderItem
from django.contrib import messages

# Create your views here.

def index(request):
    context={
        'like' : Product.objects.all()
    }
    return render(request,"web/index.html" , context)

def about(request):
    return render(request,"web/about.html")
def blog(request):
    return render(request,"web/blog.html")
def contact(request):
    return render(request,"web/contact.html")
def detail(request):
    return render(request,"web/detail.html")
def price(request):
    return render(request,"web/price.html")
def product(request):
    return render(request,"web/product.html")
def service(request):
    return render(request,"web/service.html")
def team(request):
    return render(request,"web/team.html")
def testimonial(request):
    return render(request,"web/testimonial.html")




































def login2(request):
    if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")

            user = authenticate(username=username, password=password)
            if user is not None:
                            
                    login(request, user)
                    return redirect('index')
            else:
                 messages.warning(request, 'invalid details')
                 return redirect('login')
    return render(request,"web/account/login.html")
































def sign2(request):
    if request.method=="POST":
                username=request.POST.get("username_1")
                Firstname=request.POST.get("firstname_1")
                Lastname=request.POST.get("lastname_1")
                Email=request.POST.get("email_1")
                Password=request.POST.get("password_1")
                Confirm_password=request.POST.get("confirmpassword_1")

                if Password==Confirm_password:
                      customer=User.objects.create_user(username,Email,Password)
                      customer.first_name=Firstname
                      customer.last_name=Lastname
                      customer.save()
                      return redirect('login')
    return render(request,"web/account/sign.html")












































def logout1(request):
    logout(request)
    return render(request,"web/account/login.html")




































@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")















@login_required(login_url="login")
def cart_detail(request):
    return render(request,'web/cart/cart.html')















































@login_required(login_url="login")
def checkout(request):
    return render(request, 'web/checkout.html')
















@login_required(login_url="login")
def placeorder(request):
    if request.method=="POST":
         uid=request.session.get('_auth_user_id')
         user=User.objects.get(id=uid)
         cart=request.session.get('cart')


         Firstname=request.POST.get("First_Name")
         Lastname=request.POST.get("Last_Name")
         country=request.POST.get("country")
         address=request.POST.get("address_1")
         city=request.POST.get("city_1")
         state=request.POST.get("state_1")
         postcode=request.POST.get("postcode_1")
         phone=request.POST.get("phone_1")
         email=request.POST.get("email_1")


         order_1=Order(
              user=user,
              First_Name=Firstname,
              Last_Name=Lastname,
              country=country,
              address=address,
              city=city,
              state=state,
              postcode=postcode,
              phone=phone,
              email=email
         )

         order_1.save()

         for i in cart:
              a=float(cart[i]['price'])
              b=int(cart[i]['quantity'])
              total=a*b
              order1=OrderItem(
                   order=order_1,
                   product=cart[i]['name'],
                   image=cart[i]['image'],
                   price=cart[i]['price'],
                   quantity=cart[i]['quantity'],
                   total=total
              )
              order1.save()
    return render(request, 'web/placeorder.html')





@login_required(login_url="login")
def confirm(request):
    return render(request, 'web/confirm.html')
























































