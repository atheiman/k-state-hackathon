from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Judge, Team, Review, Membership, Entrant
from .forms import CreateTeamForm, EditTeamForm, ReviewForm
from .global_vars import MEMBERS_RANGE



context_base = {}



def index(request):
    """Information about the hackathon."""
    context = context_base

    return render(request, 'hackathon/index.html', context)



@login_required
def register(request):
    """Register a team."""
    context = context_base

    if request.method == "POST":
        form = CreateTeamForm(request.POST)

        if form.is_valid():
            # process the data in form.cleaned_data
            team = Team.objects.create(
                project_name = form.cleaned_data['project_name']
                project_description = form.cleaned_data['project_description']
                project_repository = form.cleaned_data['project_repository']
            )
            team.save()

            # created team, redirect to the team page
            return HttpResponseRedirect(
                reverse('hackathon:team', args=[team.id])
            )

    else:
        form = TeamForm()

    context['form'] = form

    return render(request, 'hackathon/register.html', context)



def team(request, team_id):
    """Display team information."""
    context = context_base
    context['team'] = get_object_or_404(Team, pk=team_id)

    if request.user.username in context['team'].eids():
        # the user is a member of the team, so we will display a link to edit the team page.
        context['request_user_is_team_member'] = True

    return render(request, 'hackathon/team.html', context)



@login_required
def delete_team(request, team_id):
    """Edit team information."""
    context = context_base
    team = get_object_or_404(Team, pk=team_id)

    # this view is only for team members
    if request.user.username not in team.eids():
        return HttpResponseForbidden("""
            <h1>Forbidden</h1>
            <p>You are not a member of this team, and therefore cannot edit the team information.</p>
        """)

    return HttpResponse("Delete this team? (not implemented quite yet...)")



@login_required
def edit_team(request, team_id):
    """Edit team information."""
    context = context_base
    team = get_object_or_404(Team, pk=team_id)

    # this view is only for team members
    if request.user.username not in team.eids():
        return HttpResponseForbidden("""
            <h1>Forbidden</h1>
            <p>You are not a member of this team, and therefore cannot edit the team information.</p>
        """)

    # get the team leader
    leader = Membership.objects.filter(team=team, leader=True)

    non_leader_members = Membership.objects.filter(team=team, leader=False):

    if request.method == "POST":
        form = EditTeamForm(request.POST)

        if form.is_valid():
            # update the team fields
            team.project_name = form.cleaned_data['project_name']
            team.project_description = form.cleaned_data['project_description']
            team.project_repository = form.cleaned_data['project_repository']
            team.save()

            # member_field_prefixes = ['leader_',]
            # for i in MEMBERS_RANGE:
            #     member_field_prefixes.append('member_%d_' % i)

            # created team, redirect to the team page
            return HttpResponseRedirect(
                reverse('hackathon:team', args=[team.id])
            )

    else:
        data = {
            'project_name': team.project_name,
            'project_description': team.project_description,
            'project_repository': team.project_repository,
            'leader_eid': leader.entrant.user.username,
            'leader_year_in_school': leader.entrant.year_in_school,
            'leader_major': leader.entrant.major,
        }
        # add non_leader_members to data
        for m in non_leader_members:
            data['member_%d_eid' % non_leader_members.index(m) + 2] = m.entrant.user.username
            data['member_%d_year_in_school' % non_leader_members.index(m) + 2] = m.entrant.year_in_school
            data['member_%d_major' % non_leader_members.index(m) + 2] = m.entrant.major

        form = EditTeamForm(data)

    context['form'] = form

    return render(request, 'hackathon/edit_team.html', context)



@login_required
def review(request):
    """Judges submit reviews of the team."""
    context = context_base

    return HttpResponse('Review')
