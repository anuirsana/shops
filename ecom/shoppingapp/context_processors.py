from .models import Categary
def menu_links(request):
    links=Categary.objects.all()
    return dict(links=links)