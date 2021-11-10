from django.shortcuts import redirect, render, HttpResponseRedirect
from onlyplans.models import OnlyPlan
from events.forms import storeEventForm

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
    event = OnlyPlan.objects.filter(id=id)
    
    if event:
        context = { 'event': event[0] }
        return render(request, 'showevent.html', context)
    else:
        return HttpResponseRedirect('/')