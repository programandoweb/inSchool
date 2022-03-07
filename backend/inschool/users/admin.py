from django.contrib import admin
from .models import UserApp,TypeUserApp,GroupTypeUserApp
admin.site.register(UserApp)
admin.site.register(TypeUserApp)
admin.site.register(GroupTypeUserApp)