from django.urls import path
from user.views import RegisterView, signup, LoginView, loggedin , ProfileUpdateView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth-register'),
    path('login/', LoginView.as_view(), name='auth-login'),
    path('update/', ProfileUpdateView.as_view(), name='profile'),

    path('signedup/', signup, name='auth-signup'),
    path('loggedin/', loggedin, name='auth-login'),

]