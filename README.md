#FistDjango_24082025

## Инструкция по развертыванию проекта
1. Создать виртуальное окружение

python3 -m venv django_venv

2. активировать виртуальное окружение

sourse django_venv/bin/activate

3.Установить нужные библиотеки в виртуальное окружение

pip instal -r requirements.txt

4.Применить миграцию
'''
python manage.py migrate
'''

5.Запуск сервера
'''
python manage.py runserver
'''

## Запуск  'ipython' в контехте 'django' приложений
'''
python manage.py shell_plus --ipython
'''


## Дополнительно
1. полезное разширение для шаблонов: 'django'
'''
ext install batisteo.vscode-django
'''
2. Добавить в 'ettings.json'
'''
    "emmet.includeLanguages": {
        "django-html": "html"
    },
    "files.associations": {
        "*.html": "django-html"
    }
'''
