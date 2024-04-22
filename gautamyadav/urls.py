from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

from system import views
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.homepage, name='profile'),
    path('', profileListView.as_view(), name="profile"),
    path('api/accounts/', include('accounts.urls')),
    path('api/system/', include('system.urls')),
    path('blog/', TemplateView.as_view(template_name='blogs.html'), name='blog'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# git init
# git add .
# git commit -m "Initial commit"
# git push -u origin master
