from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *

from django.http import HttpResponse

def homepage(request):
    template_name = 'index.html'
    return render(request, template_name)


def track_visit(request):
    ip_address = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    requested_url = request.build_absolute_uri()

    try:
        # Save visit data to the database
        visit = Visit.objects.create(ip_address=ip_address, user_agent=user_agent, url=requested_url)
    except Exception as e:
        # Handle potential errors (e.g., database connection issue)
        return HttpResponse(f"Error: {str(e)}", status=500)

    # Your view logic here

    return render(request, 'index.html', {'visit': visit})


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
