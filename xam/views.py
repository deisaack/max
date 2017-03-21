from django.shortcuts import redirect
# from django.contrib.auth.forms import UserCreationForm
def login_redirect(request):

    return redirect('/account/login')
