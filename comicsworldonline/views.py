from django.shortcuts import render
from django.shortcuts import redirect
from comicsworldonline.models import Subscriber
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    #form = forms.EmailForm(request.GET)
    if request.method == 'POST':
        sub = Subscriber()
        email = request.POST.get('nl-email')
        sub.email = email
        sub.save()
        return redirect('index')
    else:
        return render(request, 'index.html')

def post(request):
    if request.method == 'POST':
        sub = Subscriber()
        email = request.POST.get('nl-email')
        sub.email = email
        sub.save()
        return render(request, 'post/' + post + '.html')
    else:
        return render(request, 'post/' + post + '.html')
