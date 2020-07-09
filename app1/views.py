from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import View
from app1.models import course
from app1.forms import courseform

# Create your views here.
def admin_login(request):
    return render(request,"admin.html")


def admin_login_check(request):
    na = request.POST.get("t1")
    pa = request.POST.get("t2")
    if na == "aravind" and pa == "aravind":
        return render(request,"admin_schedule.html")
    else:
        #messages.error(request,"Invalid User")
        messages.error(request,"invalid user")
        return redirect('admin_login')


def admin_schedule(request):
    cf = courseform()
    return render(request, "course_register.html", {"form": cf})
#    cf = courseform(request.post)
 #   if cf.is_valid():
  #      cf.save()
   #     return render(request,"course_register.html",{"form":cf})
    #else:
     #   return redirect("admin_schedule")
def save_course(request):
    cf = courseform(request.POST)
    if cf.is_valid():
        cf.save()
        return render(request, "admin_schedule.html",{"form":cf})
    else:
        messages.error(request, "invalid entry")
        return render(request, "course_register.html", {"form": cf})


def view_all(request):
    res = course.objects.all()
    return render(request,"view_all.html",{"data":res})


def Studentmain(request):
    return render(request,"student_main.html")
