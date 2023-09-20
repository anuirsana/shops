from django.shortcuts import render, redirect, get_object_or_404
from shoppingapp .models import Product
from .models import Cart,Cartitem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def _cart_id(request):
     cart=request.session.session_key
     if not cart:
       cart=request.session.create()
       return cart

def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))

    except Cart.DoesNotExist:

        cart=Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try :

        cartitem=Cartitem.objects.get(product=product,cart=cart)
        if cartitem.quantity < cartitem.product.stock:
         cartitem.quantity +=1
         cartitem.save()

    except Cartitem.DoesNotExist:

        cartitem=Cartitem.objects.create(product=product,quantity=1,cart=cart)
        cartitem.save()

    return redirect('cartapp:cartdetail')

def cartdetail(request,total=0,counter= 0,cartitems=None):

    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        cartitems=Cartitem.objects.filter( cart=cart,active=True)

        for cartitem in cartitems:
            total+= (cartitem.product.price * cartitem.quantity)
            counter+= cartitem.quantity

    except ObjectDoesNotExist:

       pass

    return render(request,'cart.html',dict(cartitems=cartitems,total=total,counter=counter))

def cart_remove(request,product_id):

     cart=Cart.objects.get(cart_id=_cart_id(request))
     product=get_object_or_404(Product,id=product_id)
     cartitem=Cartitem.objects.get(product=product,cart=cart)
     if cartitem.quantity > 1:
         cartitem.quantity -=1
         cartitem.save()
     else:
         cartitem.delete()

     return redirect('cartapp:cartdetail')

def full_remove(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cartitem = Cartitem.objects.get(product=product, cart=cart)
    cartitem.delete()
    return redirect('cartapp:cartdetail')