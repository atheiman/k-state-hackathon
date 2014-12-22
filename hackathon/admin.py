from django.contrib import admin
from .models import Judge, Entrant, Team, Vote



class JudgeAdmin(admin.ModelAdmin):
    pass



class EntrantAdmin(admin.ModelAdmin):
    pass



class TeamAdmin(admin.ModelAdmin):
    pass



class VoteAdmin(admin.ModelAdmin):
    pass



admin.site.register(Judge, JudgeAdmin)
admin.site.register(Entrant, EntrantAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Vote, VoteAdmin)
