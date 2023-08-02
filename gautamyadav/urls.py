from django.urls import path
from system import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage')
]
# git init
# git add .
# git commit -m "Initial commit"
# git push -u origin master
# git push -u origin master