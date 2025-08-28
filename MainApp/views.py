from django.shortcuts import render
from django.http import HttpResponse

user_dt = {
    "name": "Иван",
    "patronymic": "Николаевич",
    "surname": "Несторик",
    "phone": "8-965-293-83-12",
    "email": "vansilkn@mail.ru"
}


# Create your views here.
def home(request):
    text = """
        <h1>"Изучаем django"</h1>
        <strong>Автор</strong>: <i>Несторик И.Н.</i>
    """
    return HttpResponse(text)


def about(request):
    text = f"""
        <p>Имя: <b>{user_dt["name"]}</b></p>
        <p>Отчество: <b>{user_dt["patronymic"]}</b></p>
        <p>Фамилия: <b>{user_dt["surname"]}</b></p>
        <p>телефон: <b>{user_dt["phone"]}</b></p>
        <p>email: <b>{user_dt["email"]}</b></p>
    """
    return HttpResponse(text)
