from django.urls import path
from system import views

urlpatterns = [
    path('', views.homepage),
    path('<int:timeframe>', views.goals_by_int_timeframe),
    path('<str:timeframe>', views.goals_by_timeframe, name='namedurl'),
]
