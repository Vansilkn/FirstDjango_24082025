from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


items = [
    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
    {"id": 7, "name": "Картофель фри" ,"quantity":0},
    {"id": 8, "name": "Кепка" ,"quantity":124},
]



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
    """ Выводим данные словаря (который вложенный в список) по значению id"""
    for item in items:
        if item["id"] == item_id:
            context = {
                "item": item
            } 
            return render(request, "item_page.html", context)
    return render(request, "errors.html", {"errors": [f"""Товар с id={item_id} не найден"""]})


def get_items(request):
    """ Выводим данные по значению id """
    context = {
        'items': items
    } 
    return render(request, "items_list.html", context)
