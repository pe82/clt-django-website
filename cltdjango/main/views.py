from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('main/index.html')
    context = {
        'greeting': "Hello, world! Welcome to Charlotte Django Meetup's website. Please pardon our construction and check back soon.",
    }
    return HttpResponse(template.render(context, request))


def active_members(request):
    template = loader.get_template('main/active_members.html')
    context = {
        'title': "Active members of Charlote Django Meetup",
    }
    return HttpResponse(template.render(context, request))
