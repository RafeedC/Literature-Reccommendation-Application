from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

def home(request):
    return render(request, 'literature_recommendation/home.html')

def book_swiping(request):
    return render(request, 'literature_recommendation/book_swiping.html')

def my_list(request):
    return render(request, 'literature_recommendation/my_list.html')

def my_likes(request):
    return render(request, 'literature_recommendation/my_likes.html')

def my_profile(request):
    return render(request, 'literature_recommendation/my_profile.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after sign up
    template_name = 'literature_recommendation/signup.html'  # Your sign-up template

    def form_valid(self, form):
        # Save the new user first
        user = form.save()
        # Then log the user in
        login(self.request, user)
        return redirect('home')  # Redirect to home page after sign up
