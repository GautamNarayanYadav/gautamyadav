from django.urls import path, include
from django.contrib import admin

from system import views
from accounts.views import *
from system.views import track_visit

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.homepage, name='profile'),
    path('', profileListView.as_view(), name="profile"),
    path('api/accounts/', include('accounts.urls')),
    path('api/system/', include('system.urls')),
    path('track-visit/', track_visit, name='track-visit'),
]

# git init
# git add .
# git commit -m "Initial commit"
# git push -u origin master
# git push -u origin master