from django.urls import path, include
from django.contrib import admin

from system import views
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.homepage, name='profile'),
    path('', profileListView.as_view(), name="profile"),
    path('api/accounts/', include('accounts.urls')),
    path('api/system/', include('system.urls')),
]

# git init
# git add .
# git commit -m "Initial commit"
# git push -u origin master
# git push -u origin master