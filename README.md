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

### common

- Common models and views for REST API service.
- AbstractModel and User models for reusability. 
- Check http://127.0.0.1:8000/common/ for a try or documentation.


### commerce

- Commerce and community REST API service.
- See an [ER diagram](https://drive.google.com/file/d/1k1XX69KLpbbSZQdGX8mZZTHk8nDPYu1D/view?usp=sharing) or a [Sequence diagram](https://drive.google.com/file/d/1zqZskNT3qQ0gfMXErB9omCamHtPNo-h2/view?usp=sharing) for more information.
- Check http://127.0.0.1:8000/commerce/ for a try or documentation.


### snippets

- Simple code highlighting REST API service.
- Clone coding for [Django REST framework official tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/).
- Check http://127.0.0.1:8000/snippets/ for a try or documentation.
