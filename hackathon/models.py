from decimal import *

from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError

from .global_vars import YEAR_IN_SCHOOL_CHOICES, MAJOR_CHOICES, MEMBERS_RANGE



admin.site.site_header = admin.site.site_title = "K-State Hackathon Administration"
admin.site.index_title = "Home"



class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username



class Entrant(Person):
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        blank=True,
    )
    major = models.CharField(
        max_length=64,
        choices=MAJOR_CHOICES,
        blank=True,
    )



class Judge(Person):
    reviews = models.ManyToManyField(
        'Team',
        through="Review",
        blank=True,
    )



class Team(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    project_name = models.CharField(
        max_length=64,
    )
    project_description = models.TextField(
        blank=True,
        help_text="Explain your team's project. What need does this fill? How do you use it? What open-source technologies have you leveraged? What did you learn while working on this project? This description is a component of your team's score.",
    )
    project_repository = models.URLField(
        blank=True,
        help_text="URL of your project code repository. We recommend using <a href='https://github.com/' target='blank'>GitHub</a> for repository hosting.",
    )

    members = models.ManyToManyField(
        'Entrant',
        through='Membership',
    )

    def eids(self):
        eids = []
        for m in self.members:
            eids.append(m.user.username)

        return eids

    def clean(self):
        # if self.status == 'draft' and self.pub_date is not None:
        #     raise ValidationError('Draft entries may not have a publication date.')
        pass

    def __unicode__(self):
        return self.project_name



class Membership(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    team = models.ForeignKey(
        "Team",
    )
    entrant = models.ForeignKey(
        'Entrant',
        related_name="membership",
    )

    leader = models.BooleanField(
        default=False,
        help_text="The team leader will be the primary point of contact via <a href='http://webmail.ksu.edu'>K-State Webmail</a>."
    )



class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    judge = models.ForeignKey('Judge')
    team = models.ForeignKey('Team')

    # Scores
    presentation_score = models.PositiveSmallIntegerField(
        help_text="Project presentation and description score.",
    )
    creativity_score = models.PositiveSmallIntegerField(
        help_text="Project creativity and ambitiousness score.",
    )
    code_review_score = models.PositiveSmallIntegerField(
        help_text="Project code review score.",
    )

    notes = models.TextField(
        blank=True,
        help_text="Any notes or feedback you would like to give to the team.",
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
            (self.judge, self.team, self.average_score())



def members_changed(sender, **kwargs):
    if kwargs['instance'].members.count() not in MEMBERS_RANGE:
        raise ValidationError("Teams must have between 2 and 5 members.")

    team_lead_selected = False
    for m in kwargs['instance'].members:
        if m.leader == True:
            team_lead_selected = True
    if team_lead_selected == False:
        raise ValidationError("You must specify a team lead.")

m2m_changed.connect(members_changed, sender=Team.members.through)
