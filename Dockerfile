FROM python:3.8.16
WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ARG DJANGO_SECRET_KEY
ENV DJANGO_SECRET_KEY $DJANGO_SECRET_KEY
ARG DB_PASSWORD
ENV DB_PASSWORD $DB_PASSWORD
ARG DB_HOST
ENV DB_HOST $DB_HOST

ENV DJARF_PROD true
RUN mkdir logs
RUN python manage.py test
RUN python manage.py collectstatic --noinput

EXPOSE 8000
ENTRYPOINT gunicorn --bind 0.0.0.0:8000 --workers 8 --threads 8 djarf.wsgi
