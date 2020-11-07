from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


from .models import Profile, Site, TimePunch, Session, Organization

# Site Views

def site_index(request):
    sites = Site.objects.all().order_by('-id')
    return JsonResponse(sites)

def add_site(request):
    pass

def update_site(request):
    pass

def get_site(request, site_id):
    site = Site.objects.get(id=site_id)
    return JsonResponse(site)

# Session Views

def session_index(request):
    sessions = Session.objects.all().order_by('-id')

def add_session(request):
    pass

def update_session(request):
    pass

def get_session(request, session_id):
    session = Session.objects.get(id=site_id)
    return JsonResponse(session)

# Profile Views

def profile_index(request):
    employees = Profile.objects.all().order_by('-id')
    JsonResponse(employees)

def update_profile(request):
    pass

def get_profile(request, profile_id):
    user = Profile.objects.get(id=profile_id)
    JsonResponse(user)

# Authentication and Signup

def sign_up(request):
    pass

# Organization Views

def get_organization(request, organization_id):
    organization = Organization.objects.get(id=organization_id)
    JsonResponse(organization)

