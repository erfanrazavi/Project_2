from django.shortcuts import render



# Create your views here.
def home_views(request):
    return render(request , 'home/index.html')

def about_views(request):
    return render(request , 'home/about.html')

def take_action_views(request):
    return render(request , 'home/action.html')

def news_views(request):
    return render(request , 'home/news.html')

def doctores_views(request):
    return render(request , 'home/doctores.html')

def contact_views(request):
    return render(request , 'home/contact.html')