# Django Imports
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse
from django.contrib.auth import (authenticate, get_user_model, login, logout,)
from .forms import UserForm
from django.shortcuts import redirect
from .models import *


# Views

# Index only redirects. If there is no user session, redirect to login page.
# If there IS a session, redirect to 'surveys'
def index(request):
    if request.user.is_authenticated():
        return redirect('surveys')
    else:
        return redirect('login')

# Registration
def register(request):
    if request.user.is_authenticated():
        return redirect('index')

    form = UserForm(request.POST)
    template = loader.get_template('QTSurvey/register.html')

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('login')
    context = {'form':form}
    return HttpResponse(template.render(context,request))

# Surveys (Researcher/Subject)
def surveys(request):
    if not request.user.is_authenticated():
        return redirect('index')

    template = loader.get_template('QTSurvey/researcher-surveys.html')
    template = loader.get_template('QTSurvey/subject-available-surveys.html')

    return HttpResponse(template.render(request))

# Analytics (Researcher)
def researcher_analytics(request):
    if not (request.user.is_authenticated() and request.session.get('researcher')):
        return redirect('index')

    template = loader.get_template('QTSurvey/researcher-analytics.html')

    return HttpResponse(template.render(request))

# Subject View (Researcher)
def researcher_subjects(request):
    if not (request.user.is_authenticated() and request.session.get('researcher')):
        return redirect('index')

    template = loader.get_template('QTSurvey/researcher-subjects.html')

    return HttpResponse(template.render(request))

# Completed Surveys (Subject)
def subject_completed_surveys(request):
    if not (request.user.is_authenticated() and not request.session.get('researcher')):
        return redirect('index')

    template = loader.get_template('QTSurvey/subject-completed-surveys.html')

    return HttpResponse(template.render(request))

# Create Survey (Researcher)
def create_survey(request):
    if not (request.user.is_authenticated() and request.session.get('researcher')):
        return redirect('index')

    template = loader.get_template('QTSurvey/create-survey.html')

    return HttpResponse(template.render(request))
