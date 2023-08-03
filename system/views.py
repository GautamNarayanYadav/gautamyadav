from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *

def homepage(request):
    template_name = 'index.html'
    return render(request, template_name)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
