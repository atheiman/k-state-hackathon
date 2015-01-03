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
            name='Membership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('leader', models.BooleanField(default=False, help_text=b"The team leader will be the primary point of contact via <a href='http://webmail.ksu.edu'>K-State Webmail</a>.")),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
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
                ('year_in_school', models.CharField(blank=True, max_length=2, choices=[(b'1', b'First Year'), (b'2', b'Second Year'), (b'3', b'Third Year'), (b'4', b'Fourth Year'), (b'5', b'Fifth Year'), (b'6', b'Sixth Year or More')])),
                ('major', models.CharField(blank=True, max_length=64, choices=[(b'MANAGEMENT INFORMATION SYSTEMS', b'Management Information Systems'), (b'SOFTWARE ENGINEERING', b'Software Engineering'), (b'COMPUTER SCIENCE', b'Computer Science'), (b'INFORMATION SYSTEMS', b'Information Systems'), (b'OTHER ENGINEERING', b'Other Engineering'), (b'OTHER', b'Other')])),
            ],
            options={
            },
            bases=('hackathon.person',),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('presentation_score', models.PositiveSmallIntegerField(help_text=b'Project presentation and description score.')),
                ('creativity_score', models.PositiveSmallIntegerField(help_text=b'Project creativity and ambitiousness score.')),
                ('code_review_score', models.PositiveSmallIntegerField(help_text=b'Project code review score.')),
                ('notes', models.TextField(help_text=b'Any notes or feedback you would like to give to the team.', blank=True)),
                ('judge', models.ForeignKey(to='hackathon.Judge')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('project_name', models.CharField(max_length=64)),
                ('project_description', models.TextField(help_text=b"Explain your team's project. What need does this fill? How do you use it? What open-source technologies have you leveraged? What did you learn while working on this project? This description is a component of your team's score.", blank=True)),
                ('project_repository', models.URLField(help_text=b"URL of your project code repository. We recommend using <a href='https://github.com/' target='blank'>GitHub</a> for repository hosting.", blank=True)),
                ('members', models.ManyToManyField(to='hackathon.Entrant', through='hackathon.Membership')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='team',
            field=models.ForeignKey(to='hackathon.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='entrant',
            field=models.ForeignKey(related_name='membership', to='hackathon.Entrant'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='team',
            field=models.ForeignKey(to='hackathon.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='judge',
            name='reviews',
            field=models.ManyToManyField(to='hackathon.Team', through='hackathon.Review', blank=True),
            preserve_default=True,
        ),
    ]
