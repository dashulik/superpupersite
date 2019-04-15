from django.shortcuts import render
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'index.html')

def post(request):
    post = request.GET['post']
    return render(request, 'post/' + post + '.html')