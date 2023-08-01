from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# dictionary data store
goals = {
    'daily': 'Learn Something New',
    'weekly': 'Take a day off',
    'monthly': 'Complete a creative course'
}


def homepage(request):
    goal_list = '<html><body><ul>'
    for goal in goals.keys():
        href = reverse('namedurl', args=[goal])
        goal_list += f'<li><a href="{href}">{goal}</a></li>'
    goal_list += '</ul></body></html>'
    return HttpResponse(goal_list)


def goals_by_int_timeframe(request, timeframe):
    timeframes = list(goals.keys())
    redirect_to = timeframes[timeframe - 1]
    named_redirect = reverse('namedurl', args=[redirect_to])
    return HttpResponseRedirect(named_redirect)


def goals_by_timeframe(request, timeframe):
    goal = goals[timeframe]
    return HttpResponse(goal)





