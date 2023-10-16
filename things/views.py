from django.shortcuts import render
from django.http import HttpResponse

def home (request):     # response is an object with all the info from a http request
    return render(request, "home.html")     # uses the template to render the page