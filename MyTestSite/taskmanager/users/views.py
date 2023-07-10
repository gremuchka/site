from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# login part; imports
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# profile part; imports
from django.views.generic.detail import DetailView

from .models import ProfileUser


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account created {username}!')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
    return render(request, 'users/register.html', {'user_form': user_form})


#@login_required
#def profile(request):
    #return render(request, 'users/profile.html')


# login part; works
def log(request):
    if request.method == 'POST':
        users_form = LoginForm(request.POST)
        if users_form.is_valid():
            cd = users_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        users_form = LoginForm()
    return render(request, 'users/login.html', {'users_form': users_form})


class ShowProfilePageView(DetailView):
    model = ProfileUser
    template_name = 'base/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = ProfileUser.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(ProfileUser, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
