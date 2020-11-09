from django.contrib import admin
from .models import Site, Profile, TimePunch, Organization, Session

# Register your models here.

admin.site.register(Profile)
admin.site.register(Site)
admin.site.register(TimePunch)
admin.site.register(Organization)
admin.site.register(Session)