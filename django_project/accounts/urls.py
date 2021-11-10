from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('<username>', views.ProfileView.as_view(), name='profile'),
    path('login/',views.CustomLoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
]