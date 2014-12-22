from decimal import *

from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User, Group

from .global_vars import SCHOOL_STATUS_CHOICES, MAJOR_CHOICES



admin.site.site_header = admin.site.site_title = "K-State Hackathon Administration"
admin.site.index_title = "Home"



class Person(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(
        max_length=12,
        blank=True,
        help_text="ten digit phone number, xxx-xxx-xxxx",
    )

    def __unicode__(self):
        return self.user.username



class Judge(Person):
    votes = models.ManyToManyField('Team', through="Vote")



class Entrant(Person):
    school_status = models.CharField(
        max_length=30,
        choices=SCHOOL_STATUS_CHOICES,
        blank=True,
        help_text="What is your school standing?",
    )
    major = models.CharField(
        max_length=40,
        choices=MAJOR_CHOICES,
        blank=True,
        help_text="What is your undergraduate major?",
    )
    team = models.ForeignKey(
        'Team',
        blank=True,
        null=True,
    )

    def is_upperclass(self):
        if self.school_status not in ['1','2']:
            return True
        else:
            return False



class Team(models.Model):
    project_name = models.CharField(
        max_length=40,
        blank=True,
    )
    project_description = models.TextField(
        blank=True,
        help_text="Explain your team's project. What need does this fill? How do you use it? What open-source technologies have you leveraged? What did you learn while working on this project?",
    )
    project_repository = models.URLField(
        blank=True,
        help_text="URL of your project code repository. We recommend using <a href='https://github.com/' target='blank'>GitHub</a> for repository hosting.",
    )
    leader = models.ForeignKey(
        Entrant,
        related_name="leader_of",
        help_text="The team leader will be the primary contact for the project.",
    )

    def __unicode__(self):
        return self.project_name



class Vote(models.Model):
    judge = models.ForeignKey('Judge')
    team = models.ForeignKey('Team')

    # Scores
    presentation_score = models.PositiveSmallIntegerField(
        help_text="Project presentation and description score."
    )
    creativity_score = models.PositiveSmallIntegerField(
        help_text="Project creativity and ambitiousness score."
    )
    code_review_score = models.PositiveSmallIntegerField(
        help_text="Project code review score."
    )

    def average_score(self):
        getcontext().prec = 3
        return Decimal(
            self.presentation_score +
            self.creativity_score +
            self.code_review_score
        ) / 3

    def __unicode__(self):
        return "User: %s; Team: %s; Avg Score: %d" % \
            (self.user, self.team, self.average_score)
