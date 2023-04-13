FROM python:3.8.16
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV DJARF_PROD true
CMD python manage.py collectstatic
EXPOSE 8000
ENTRYPOINT python manage.py runserver 0.0.0.0:8000
