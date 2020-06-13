from django.http import HttpResponse

from . import sender


def index(request):
    sender.send_email("Test topic", "test message")
    return HttpResponse("Hello, world. You're at the polls index.")
