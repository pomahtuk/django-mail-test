Simple showcase for django email sending.

Using default SMTP backend and Yandex, effectively a way to send an email from own inbox to won inbox.

## Running locally

```
EMAIL_USER=<user> EMAIL_PASSWORD=<pwd> python manage.py runserver
```

## Running with Docker

```bash
docker build -t django-sender .
docker run -it -p 8000:80 -e EMAIL_USER=<user> -e EMAIL_PASSWORD=<pwd> django-sender
```

## Sending

```bash
curl localhost:8000/email
```