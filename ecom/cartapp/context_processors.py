from cartapp.models import Cart,Cartitem
from cartapp.views import _cart_id


def counter(request):
    itemcount=0
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            cartitems=Cartitem.objects.all().filter(cart=cart[:1])
            for cartitem in cartitems:
                itemcount +=cartitem.quantity
        except Cart.DoesNotExist:
            itemcount=0
    return  dict(itemcount=itemcount)

