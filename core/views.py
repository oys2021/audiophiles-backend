from django.shortcuts import render

# Create your views here.
def api_root(request):
    return render(request, 'core/api_home.html')