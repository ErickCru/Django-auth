from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = 'login/index.html'


def LogOut(request):
    logout(request)
    return redirect('accounts/login/')
