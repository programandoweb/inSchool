from django.contrib import admin
from .models import UserApp,TypeUserApp,GroupTypeUserApp

"""Change inputs in admin view"""
#class UserAppAdmin(admin.ModelAdmin):
#    fields = ['names', 'email']
#admin.site.register(UserApp, UserAppAdmin)

class TypeUserAppInline(admin.StackedInline):
    model = TypeUserApp
    extra = 1

class GroupTypeUserAppAdmin(admin.ModelAdmin):
    inlines = [TypeUserAppInline]

admin.site.register(UserApp)
admin.site.register(TypeUserApp)
admin.site.register(GroupTypeUserApp,GroupTypeUserAppAdmin)