from django.shortcuts import render

# Create your views here.

def pedro (request):
    return render(request, 'pedro_jackson/pedro.html')