from django.shortcuts import render

# Create your views here.
def register(req):
    context = {}
    return render(req, 'Users/register.html', context)