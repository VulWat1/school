from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/MainPage.html')
def about(request):
    return render(request, 'main/AboutPage.html')
def features(request):
    return render(request, 'main/Features.html')