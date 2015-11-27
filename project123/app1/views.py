from django.shortcuts import render
from django.http import HttpResponse
from models import User, Group, Message


def Index(request):
    msgs = Message.objects.all().order_by('ts')[:10]
    response = "<br>".join(m.__unicode__() for m in msgs)
    return HttpResponse('Hello world <br> %s' % response )
# Create your views here.
