from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def home(request):
    context = {
        "name":"Несторик Иван Николаевич",
        "email":"vansilkn@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
    user_dt = {
        "name": "Иван",
        "patronymic": "Николаевич",
        "surname": "Несторик",
        "phone": "8-965-293-83-12",
        "email": "vansilkn@mail.ru"
        } 
    context = {
        'user_dt': user_dt
    } 
    return render(request, "about.html", context)


def get_item(request, item_id:int ):
    """ Get alitem by id from db. """
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return render(request, "errors.html", {"errors": [f"""Товар с id={item_id} не найден"""]})
    else:
        context = {"item": item} 
        return render(request, "item_page.html", context)
    


def get_items(request):
    """ Get all items from db. """
    items = Item.objects.all()
    context = {'items': items} 
    return render(request, "items_list.html", context)
