from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User, Entrant, Judge, Team, Review



class TeamAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created',
    ]
    list_display = [
        'project_name',
        'created',
    ]



class EntrantAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created',
    ]
    list_display = [
        # 'user.username',
        # 'user.first_name',
        # 'user.last_name',
        'user',
        'membership',
        'created',
    ]



class JudgeAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created',
    ]
    list_display = [
        # 'user.username',
        # 'user.first_name',
        # 'user.last_name',
        'user',
        'created',
    ]



class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created',
    ]
    list_display = [
        'team',
        'judge',
        'average_score',
    ]



# admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Entrant, EntrantAdmin)
admin.site.register(Judge, JudgeAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Review, ReviewAdmin)
