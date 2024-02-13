from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def homepage(request):
    template_name = 'index.html'
    return render(request, template_name)


def track_visit(request):
    ip_address = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    requested_url = request.build_absolute_uri()

    logger.info(f"Visit from IP: {ip_address}, User-Agent: {user_agent}, URL: {requested_url}")

    # Your view logic here

    return HttpResponse("Hello, welcome to the site!")


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
