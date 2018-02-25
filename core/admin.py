from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SiteSettings

admin.site.register(SiteSettings, SingletonModelAdmin)
