from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class LoginUserView(View):
    template = 'login_user.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/principal')
        return render(request, self.template)
