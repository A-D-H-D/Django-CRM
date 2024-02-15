from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    # check to see if they are logging in
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, ('You have been logged in'))

            return redirect('home')
        else:
            messages.error(request, ('Error logging in - please try again...'))
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

# def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, ('you have been logged out'))
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})


def customer_record(request, pk):
      if request.user.is_authenticated:
            # look up record
            customer_record = Record.objects.get(id = pk)
            return render(request, 'record.html', {'customer_record':customer_record})
      else:
            messages.error(request, ('you must be logged it to view a record'))
            return redirect('home')
      

def delete_record(request, pk):
      if request.user.is_authenticated:   
        delete_it  = Record.objects.get(id = pk)
        delete_it.delete()
        messages.error(request, ('Record has been deleted'))
        return redirect('home')
      else:
            messages.error(request, ('you must be logged it to delete a record'))
            return redirect('home')
      

def add_record(request):
      form =  AddRecordForm(request.POST or None)
      if request.user.is_authenticated:
            if request.method == 'POST':
                  if form.is_valid():
                        add_record = form.save()
                        messages.success(request, ('Record has been added'))
                        return redirect('home')      
            return render(request, 'add_record.html', {'form': form})
      else:
            messages.error(request, ('you must be logged it to add a record'))
            return redirect('home')            