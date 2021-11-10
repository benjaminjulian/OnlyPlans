from django.shortcuts import render, HttpResponseRedirect
from onlyplans.models import FriendMgmt, Profile
from django.db import models
from onlyplans.forms import FriendMgmtForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        if request.user.get_full_name() != "":
            context = {'name': request.user.get_full_name()}
        else:
            context = {'name': request.user.username}
        return render(request, "index.html", context)
    else:
        return HttpResponseRedirect('/accounts/')

@login_required
def my_friends(request):
    """
        used for Displaying and managing friends
    """
    if request.method == 'POST':

        form = FriendMgmtForm(request.POST)
        if form.is_valid():

            user = models.User.objects.get(id=80)
            friend_manage = FriendMgmt(user=request.user, friend= user)
            friend_manage.save()

            return HttpResponseRedirect('/friends/')

    #else:
    #    form = PdfValidationForm()

    user = request.user
    profile = Profile.objects.get(user=user)
    full_name = user.get_full_name()
    friends = FriendMgmt.objects.filter(user=request.user)


    return render(request, 'friends.html', {'form': form,
                                        'full_name':full_name,
                                        'friends':friends,
                                        }
                            )