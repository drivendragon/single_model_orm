from django.shortcuts import render, redirect
import random
from .models import Users


# show all of the data from a table
def index(request):
    context = {
    	"all_users": Users.objects.all()
    }
    return render(request, "index.html", context)


def register(request):
    print('ok start')
    newly_created_user = Users(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'], age=request.POST['age'])
    newly_created_user.save()
    print('ok end')
    return redirect('/')