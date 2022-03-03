from django.shortcuts import render

def pre_deploy(request):
    return render(request, 'core/pre_deploy.html', {})