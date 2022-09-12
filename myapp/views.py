from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):   
    # feature1 = Feature()
    # feature1.id = 1
    # feature1.name = "Gagan"
    # feature1.is_true = True
    # feature1.details = "first feature"

    # feature2 = Feature()
    # feature2.id = 2
    # feature2.name = "Gagan again"
    # feature2.is_true = True
    # feature2.details = "second feature"

    # feature3 = Feature()
    # feature3.id = 3
    # feature3.name = "Gagan firse"
    # feature3.is_true = False
    # feature3.details = "third feature"

    # feature4 = Feature()
    # feature4.id = 4
    # feature4.name = "Gagan baap re"
    # feature4.is_true = True
    # feature4.details = "fourth feature"

    # features = [feature1, feature2, feature3, feature4]  

    features = Feature.objects.all()    # fetching from database
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password is not same')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    # text = request.POST['text']
    # amount_of_words = len(text.split())
    posts =  [1, 2, 3, 4, 'gagan', 'piddi']
    # return render(request, 'counter.html', {'amount': amount_of_words})
    return render(request, 'counter.html', {'posts': posts})

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})