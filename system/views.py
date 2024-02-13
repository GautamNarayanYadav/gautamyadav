from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import *

from django.http import HttpResponse

def homepage(request):
    template_name = 'index.html'
    return render(request, template_name)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
