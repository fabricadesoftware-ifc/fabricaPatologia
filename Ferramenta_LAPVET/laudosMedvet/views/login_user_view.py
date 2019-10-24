from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import Group, User

class LoginUserView(View):
    template = 'login_user.html'

    def get(self, request):
        model = User.objects.all()
        if request.user.is_authenticated:
            return HttpResponseRedirect('/principal')
        return render(request, self.template, {'model':model})
