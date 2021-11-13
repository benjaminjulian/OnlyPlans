from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from friendship.models import Friend, FriendshipRequest

# Create your views here.
def myfriends(request):
    if request.user.is_authenticated:
        friends = Friend.objects.friends(request.user)

        if request.user.get_full_name() != "":
            name = request.user.get_full_name()
        else:
            name = request.user.username
        
        requests = Friend.objects.unrejected_requests(user=request.user)

        context = { 'name': name, 'friends': friends, 'requests': requests }
        return render(request, "myfriends.html", context)
    else:
        return HttpResponseRedirect('/accounts/')

def askfriend(request, other):
    if request.user.is_authenticated:
        other_qs = User.objects.filter(username=other)
        
        if other_qs.count() > 0:
            person = other_qs[0]
            Friend.objects.add_friend(request.user, person)
        return HttpResponseRedirect('/user/' + person.username)
    else:
        return HttpResponseRedirect('/accounts/')

def unfriend(request, other):
    if request.user.is_authenticated:
        person_qs = User.objects.filter(username=other)
        
        if person_qs.count() > 0:
            person = person_qs[0]
            Friend.objects.remove_friend(request.user, person)
            return HttpResponseRedirect('/user/' + person.username)

def cancelrequest(request, id):
    if request.user.is_authenticated:
        f_request = get_object_or_404(
            request.user.friendship_requests_sent,
            id=id)
        other = f_request.to_user
        f_request.cancel()
    return HttpResponseRedirect('/user/' + other.username)

def registerfriend(request, id):
    if request.user.is_authenticated:
        f_request = get_object_or_404(
            request.user.friendship_requests_received,
            id=id)
        other = f_request.from_user
        f_request.accept()
    return HttpResponseRedirect('/user/' + other.username)

def viewperson(request, person_username):
    if request.user.is_authenticated:
        person_qs = User.objects.filter(username=person_username)
        
        if person_qs.count() > 0:
            person = person_qs[0]

            if person == request.user:
                return HttpResponseRedirect('/user/')
            else:
                are_friends = Friend.objects.are_friends(request.user, person) == True

                sent_requests = Friend.objects.sent_requests(user=request.user)
                received_requests = Friend.objects.unrejected_requests(user=request.user)

                friend_request = { 'request_sent': False, 'request_received': False }
                
                for sent_request in sent_requests:
                    if sent_request.to_user == person:
                        friend_request = { 'request_sent': True, 'request_received': False, 'f_request': sent_request }
                for received_request in received_requests:
                    if received_request.to_user == request.user:
                        friend_request = { 'request_sent': False, 'request_received': True, 'f_request': received_request }

                if person.get_full_name() != "":
                    person_name = person.get_full_name()
                else:
                    person_name = person.username
                
                context = {'person_name': person_name, 'person_username': person.username, 'are_friends': are_friends, 'friend_request': friend_request }
                return render(request, "person.html", context)
        else:
            return HttpResponseRedirect('')
    else:
        return HttpResponseRedirect('/accounts/')