from django.shortcuts import render, redirect
from . models import Student
from django.contrib import messages


def home(request):
    std=Student.objects.all()  # Retrieves all 'Student' objects from the database using the 'objects.all' method of student model.
    print(std)
    return render(request,"std/home.html",{'std':std})  #({'std': std}):The context dictionary contains key-value pairs where keys represent variable names accessible in the template, 
                                                        #and values are the data passed from the view.

def std_add(request):
    if request.method=='POST':
        print("Added Successfully")
        # retrieve the user inputs
        stds_roll=request.POST.get("std_roll")         # Retrieves the value of the std_roll field from the POST data.
        stds_name=request.POST.get("std_name")         # Request_post is a dictionary like object containing the data submitted in the form.
        stds_email=request.POST.get("std_email")       # The get() method retrieves the value associated with the key 'std_roll'.
        stds_mobile=request.POST.get("std_mobile")
        stds_address=request.POST.get("std_address")

        #create an objects for models
        s=Student()              # Creates a new instances of the 'Student' model. This creates an empty Student object in memory.
        s.roll=stds_roll
        s.name=stds_name
        s.email=stds_email
        s.mobile=stds_mobile
        s.address=stds_address

        s.save()
        return redirect('/')

    return render(request,"std/add_std.html",{})

def delete_std(request,roll):
    s=Student.objects.get(pk=roll)    # Retrieves the 'Student' object from the database whose primary key(pk) matches the provided 'roll' value.
    s.delete()
    messages.add_message(request, messages.SUCCESS,'Your Account has been Deleted Successfully !!!')
    return redirect("/")

def update_std(request,roll):
    std=Student.objects.get(pk=roll)

    return render(request,"std/update_std.html",{'std':std})

def do_update_std(request,roll):
    std_roll=request.POST.get("std_roll")
    std_name=request.POST.get("std_name")
    std_email=request.POST.get("std_email")
    std_mobile=request.POST.get("std_mobile")
    std_address=request.POST.get("std_address")

    std=Student.objects.get(pk=roll)

    std.roll=std_roll
    std.name=std_name
    std.email=std_email
    std.mobile=std_mobile
    std.address=std_address
    messages.add_message(request, messages.SUCCESS,'Your Account has been Updated Successfully !!!')

    std.save()
    return redirect("/")  #Redirect to home page.
