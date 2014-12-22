from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Judge, Entrant, Team, Vote



context_base = {}



def index(request):
    pass



def register_entrant(request):
    pass



def register_team(request):
    pass



def vote(request):
    pass

