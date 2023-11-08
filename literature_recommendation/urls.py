from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book_swiping/', views.book_swiping, name='book_swiping'),
    path('my_list/', views.my_list, name='my_list'),
    path('my_likes/', views.my_likes, name='my_likes'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('login/', LoginView.as_view(template_name='literature_recommendation/login.html'), name='login'),  # Use the built-in view
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Use the built-in view
    path('signup/', views.SignUpView.as_view(), name='signup'),  # Your custom sign-up view


]