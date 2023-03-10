from django.shortcuts import render
from .models import Forms
# Create your views here.
def index(request):
    return render(request, 'index.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        if User.objects.filter(email = email).exists():
            messages.info(request, "email already exists")
            return redirect('/')
        elif User.objects.filter(phone = phone):
            messages.info(request, "phone already exists")
            return redirect('/')
        
        
##################### REGISTRATION IS NOT DONE YET ##########################