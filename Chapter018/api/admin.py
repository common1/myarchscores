from django.contrib import admin
from api.models import (
    Club,
    Membership,
    User,
)

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

class ClubAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline
    ]

admin.site.register(Club, ClubAdmin)
# admin.site.register(Membership)
admin.site.register(User)

