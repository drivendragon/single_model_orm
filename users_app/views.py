from django.shortcuts import render, redirect
import random
from .models import Users

#def index(request):
 #   return render(request, "index.html")

# show all of the data from a table
def index(request):
    context = {
    	"all_users": Users.objects.all()
    }
    return render(request, "index.html", context)


def register(request):
   # newly_created_user = Users.objects.create(first_name="aa",last_name="ddd",email_address="email@l.com",age=98)
   # print(newly_created_user.id)	
    #first_name = Users.objects.first()
    print('ok start')
    #user_instance = Users.objects.create(first_name='first_name', last_name='last_name', email_address="email_address",age=int("age"))
    #return render(request, 'some_name.html.html')
    # if request.POST['first_Name'] != '':
     context = {
        'first_name': first_name,
        'last_name': last_name
    }
   # newly_created_user = Users(first_name='first_name', last_name='last_name', email_address='email_address', age=33)
    
    newly_created_user.save()
    #first_name = Users.objects.create()
    #models.age('age'), max_length=5, Null=True,
   #blank=True)
    print('ok end')
  #  return render(request, 'index.html', context)
    return redirect('/', context)