"""Build some test teams."""

import json

from hackathon.models import *



sample_data_path = 'hackathon/sample_data.json'

with open(sample_data_path) as data_file:
    sample_data = json.load(data_file)

print "Deleting all non-superuser Users."

User.objects.filter(is_superuser=False).delete()
Team.objects.all().delete()

print "Done."

print "Attempting to create %d Entrants." % len(sample_data['entrants'])

for e in sample_data['entrants']:
    new_user = User.objects.create(
        username=e['username'],
        first_name=e['first_name'],
        last_name=e['last_name'],
        email=e['email'],
    )
    new_user.set_password(e['password'])
    new_user.save()

    new_entrant = Entrant.objects.create(
        user=new_user,
        year_in_school=str(e['year_in_school']),
        major=e['major'],
    )
    new_entrant.save()
    print '.'

print 'Done.'



print "Attempting to create %d Judges." % len(sample_data['judges'])

for j in sample_data['judges']:
    new_user = User.objects.create(
        username=j['username'],
        first_name=j['first_name'],
        last_name=j['last_name'],
        email=j['email'],
    )
    new_user.set_password(j['password'])
    new_user.save()

    new_judge = Judge.objects.create(
        user=new_user,
    )
    new_entrant.save()
    print '.'

print 'Done.'



print "Attempting to create %d Teams." % len(sample_data['teams'])

for t in sample_data['teams']:
    new_team = Team.objects.create(
        project_name=t['project_name'],
        project_description=t['project_description'],
        project_repository=t['project_repository'],
    )
    for m in t['members']:
        # members is a list of usernames
        membership = Membership(
            team=new_team,
            entrant=Entrant.objects.get(user=User.objects.get(username=m)),
        )
        if t['members'].index(m) == 0:
            # the first username in members list will be leader of team
            membership.leader = True
        membership.save()
    print '.'

print 'Done.'



print "Attempting to create %d Reviews." % len(sample_data['reviews'])

for r in sample_data['reviews']:
    new_review = Review.objects.create(
        judge=Judge.objects.get(user=User.objects.get(username=r['judge'])),
        team=Team.objects.get(project_name=r['team']),
        presentation_score=r['presentation_score'],
        creativity_score=r['creativity_score'],
        code_review_score=r['code_review_score'],
        notes=r['notes'],
    )
    print '.'

print 'Done.'
