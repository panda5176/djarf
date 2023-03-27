# djarf

Django applications with REST framework


## Quickstart

```sh
git clone https://github.com/panda5176/djarf
cd djarf
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # admin:password123
python manage.py runserver
http -a admin:password123 POST http://127.0.0.1:8000/snippets/ code="print(123)"
```


## Applications

### snippets

- Simple code highlighting web REST API.
- Clone coding for [Django REST framework official tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/).
- Check http://127.0.0.1:8000/snippets/ for documentation.
