from django.shortcuts import render, redirect
from . models import Student
from django.contrib import messages


# Create your views here.

def home(request):
    std=Student.objects.all()
    print(std)
    # messages.add_message(request, messages.SUCCESS,'Your Account has been Created Successfully !!!')

    return render(request,"std/home.html",{'std':std})

def std_add(request):
    if request.method=='POST':
        print("Added Successfully")
     #retrieve the user inputs
        stds_roll=request.POST.get("std_roll")
        stds_name=request.POST.get("std_name")
        stds_email=request.POST.get("std_email")
        stds_mobile=request.POST.get("std_mobile")
        stds_address=request.POST.get("std_address")

        #create an objects for models
        s=Student()
        s.roll=stds_roll
        s.name=stds_name
        s.email=stds_email
        s.mobile=stds_mobile
        s.address=stds_address

        s.save()
        return redirect('/')

    return render(request,"std/add_std.html",{})

def delete_std(request,roll):
    s=Student.objects.get(pk=roll)
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
