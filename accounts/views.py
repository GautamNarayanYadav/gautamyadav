from django.views.generic import ListView
from rest_framework import viewsets, permissions, authentication

from .models import *
from .serializers import *


class ProfileViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated, )
    # authentication_classes = (authentication.TokenAuthentication, )
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class profileListView(ListView):
    template_name = "index.html"
    context_object_name = "profile"
    model = Profile

    # def get_context_data(self, **kwargs):
    #     context = super(profileListView, self).get_context_data(**kwargs)
    #     context['profiles'] = Profile.objects.all().last()
    #     return context
