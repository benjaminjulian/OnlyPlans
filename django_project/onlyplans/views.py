from django.shortcuts import render, HttpResponseRedirect
from onlyplans.models import Profile
from django.db import models
from onlyplans.forms import FriendMgmtForm
from django.contrib.auth.decorators import login_required
from onlyplans.models import OnlyPlan
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        var_from = datetime.now()
        var_to = var_from + timedelta(days=7)
        plans = OnlyPlan.objects.filter(when__range=[var_from, var_to]).order_by("when")
        if request.user.get_full_name() != "":
            context = { 'name': request.user.get_full_name(), 'plans': plans }
        else:
            context = { 'name': request.user.username, 'plans': plans }
        return render(request, "index.html", context)
    else:
        return HttpResponseRedirect('/accounts/')