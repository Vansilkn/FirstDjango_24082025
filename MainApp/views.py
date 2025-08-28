from django.shortcuts import render
from django.http import HttpResponse


user_dt = {
    "name": "Иван",
    "patronymic": "Николаевич",
    "surname": "Несторик",
    "phone": "8-965-293-83-12",
    "email": "vansilkn@mail.ru"
}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


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


def get_items(request, items_id:int):
    for item in items:
        if item["id"] == items_id:
            text = f"""
                <div style="font-family:Impact,Arial, Verdana;
                            font-size: 18px;
                            border: 1px solid red;
                            border-radius: 20px;
                            background: #d9d9d9;
                            width: calc(30%);
                            min-width: 200px;
                            padding: 10px
                            ">
                    <p>
                        Имя: <i><u style="color: red">{item['name']}</u></i>
                    </p>
                    <p>
                        Количество: <i><u  style="color: red">{item['quantity']}</u></i>
                    </p>
                </div>
            """
            return HttpResponse(text)
    
