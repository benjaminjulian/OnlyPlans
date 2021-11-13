from django.urls import path
from . import views

urlpatterns = [
    path('', views.myfriends),
    path('friend/<other>', views.askfriend),
    path('unfriend/<other>', views.unfriend),
    path('accept/<id>', views.registerfriend),
    path('cancelrequest/<id>', views.cancelrequest),
    path('<person_username>', views.viewperson),
]
