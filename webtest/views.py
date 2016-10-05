from django.shortcuts import render
from django.shortcuts import render_to_response
from models import posts
# Create your views here.
def home(request):
    return render_to_response('index.html')
