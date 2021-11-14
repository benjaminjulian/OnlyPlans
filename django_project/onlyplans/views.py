from django.shortcuts import render, HttpResponseRedirect
from onlyplans.models import OnlyPlan
from datetime import datetime, timedelta
from friendship.models import Friend, Follow, Block
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    var_from = datetime.now()
    var_to = var_from + timedelta(days=7)

    plans = OnlyPlan.objects.filter(when__range=[var_from, var_to]).order_by("when")

    excludes = []

    for plan in plans:
        event_owner_qs = User.objects.filter(username=plan.owner)
        if event_owner_qs:
            event_owner = event_owner_qs[0]

            can_see_event = False
            if not request.user.is_authenticated:
                can_see_event = False
            elif not plan.friendsonly:
                can_see_event = True
            elif Friend.objects.are_friends(request.user, event_owner):
                can_see_event = True
            elif event_owner == request.user:
                can_see_event = True
            
            if not can_see_event:
                excludes.append(plan.id)
    
    plans = plans.exclude(id__in=excludes)

    if request.user.is_authenticated:
        if request.user.get_full_name() != "":
            name = request.user.get_full_name()
        else:
            name = request.user.username
    else:
        name = ''

    context = { 'name': name, 'plans': plans }

    return render(request, "index.html", context)