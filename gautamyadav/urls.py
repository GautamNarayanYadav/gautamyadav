from django.urls import path
from system import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('<int:timeframe>', views.goals_by_int_timeframe),
    path('<str:timeframe>', views.goals_by_timeframe, name='namedurl'),
]
# git init
# git add .
# git commit -m "Initial commit"
# git push -u origin master