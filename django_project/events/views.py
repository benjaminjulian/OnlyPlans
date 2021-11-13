from django.shortcuts import redirect, render, HttpResponseRedirect
from onlyplans.models import OnlyPlan
from events.forms import storeEventForm
from friendship.models import Friend
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = storeEventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            return redirect('/')
    else:
        form = storeEventForm()
    return render(request, 'events.html', {'form': form})

def display(request, id):
    event_qs = OnlyPlan.objects.filter(id=id)
    
    if event_qs:
        event = event_qs[0]
        event_owner_qs = User.objects.filter(username=event.owner)

        can_see_event = False

        if event_owner_qs:
            event_owner = event_owner_qs[0]
            if not event.friendsonly:
                can_see_event = True
            elif Friend.objects.are_friends(request.user, event_owner):
                can_see_event = True
            elif event_owner == request.user:
                can_see_event = True
            
            if can_see_event:
                if event_owner.get_full_name() != "":
                    person_name = event_owner.get_full_name()
                else:
                    person_name = event_owner.username

                context = { 'event': event, 'owner': person_name }
                return render(request, 'showevent.html', context)

    return HttpResponseRedirect('/')