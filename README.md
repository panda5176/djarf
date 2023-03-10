# djarf

Django application with REST framework


## Quickstart

```sh
$ git clone https://github.com/panda5176/djarf
$ cd djarf
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser  # admin:password123
$ python manage.py runserver
$ http -a admin:password123 POST http://127.0.0.1:8000/snippets/ code="print(123)"
```
