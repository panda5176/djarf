FROM python:3.8.16
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV DJARF_PROD true
RUN python manage.py collectstatic --noinput
EXPOSE 8000
ENTRYPOINT gunicorn --bind 0.0.0.0:8000 --workers 8 --threads 8 djarf.wsgi
