# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(help_text=b'ten digit phone number, xxx-xxx-xxxx', max_length=12, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='hackathon.Person')),
            ],
            options={
            },
            bases=('hackathon.person',),
        ),
        migrations.CreateModel(
            name='Entrant',
            fields=[
                ('person_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='hackathon.Person')),
                ('school_status', models.CharField(blank=True, help_text=b'What is your school standing?', max_length=30, choices=[(b'1', b'First Year'), (b'2', b'Second Year'), (b'3', b'Third Year'), (b'4', b'Fourth Year'), (b'5', b'Fifth Year'), (b'6+', b'Sixth Year +'), (b'GRADUATE STUDENT', b'Graduate Student')])),
                ('major', models.CharField(blank=True, help_text=b'What is your undergraduate major?', max_length=40, choices=[(b'COMPUTER SCIENCE', b'Computer Science'), (b'SOFTWARE ENGINEERING', b'Software Engineering'), (b'INFORMATION SYSTEMS', b'Information Systems'), (b'ELECTRICAL ENGINEERING', b'Electrical Engineering'), (b'COMPUTER ENGINEERING', b'Computer Engineering'), (b'ENGINEERING OTHER', b'Engineering - Other'), (b'MANAGEMENT INFORMATION SYSTEMS', b'Management Information Systems'), (b'BUSINESS OTHER', b'Business - Other'), (b'GRADUATE ENGINEERING', b'Graduate Student in Engineering'), (b'GRADUATE BUSINESS', b'Graduate Student in Business'), (b'GRADUATE OTHER', b'Graduate Student in Business'), (b'OTHER', b'Other')])),
            ],
            options={
            },
            bases=('hackathon.person',),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=40, blank=True)),
                ('project_description', models.TextField(help_text=b"Explain your team's project. What need does this fill? How do you use it? What open-source technologies have you leveraged? What did you learn while working on this project?", blank=True)),
                ('project_repository', models.URLField(help_text=b"URL of your project code repository. We recommend using <a href='https://github.com/' target='blank'>GitHub</a> for repository hosting.", blank=True)),
                ('leader', models.ForeignKey(related_name='leader_of', to='hackathon.Entrant', help_text=b'The team leader will be the primary contact for the project.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('presentation_score', models.PositiveSmallIntegerField(help_text=b'Project presentation and description score.')),
                ('creativity_score', models.PositiveSmallIntegerField(help_text=b'Project creativity and ambitiousness score.')),
                ('code_review_score', models.PositiveSmallIntegerField(help_text=b'Project code review score.')),
                ('judge', models.ForeignKey(to='hackathon.Judge')),
                ('team', models.ForeignKey(to='hackathon.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='judge',
            name='votes',
            field=models.ManyToManyField(to='hackathon.Team', through='hackathon.Vote'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entrant',
            name='team',
            field=models.ForeignKey(to='hackathon.Team', blank=True),
            preserve_default=True,
        ),
    ]
