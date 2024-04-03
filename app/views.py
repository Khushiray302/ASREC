from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.shortcuts import redirect
from datetime import date
from .models import Contact
from django import forms
from .models import Blog
from django.core.files.storage import default_storage
from django.conf import settings
import os
from django.core.files.base import File
from django.http import HttpResponse
from .models import Team, Event
# Create your views here.
def index(request):
    return render(request,'index.html')


def event(request):
    return render(request,'event.html')

def about(request):
    return render(request,'about.html') 

def login_admin(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error ="yes"
        except:
            error = "yes"
    return render(request,'login_admin.html', locals())


def Logout(request):
    logout(request)
    return redirect('login_admin')
def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    else:
        return  render(request,"admin_home.html")
    
def member(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    else:
        return  render(request,"member.html")


def contact(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fullname']
        em = request.POST['email']
        m = request.POST['mobile']
        s = request.POST['subject']
        msg = request.POST['message']
        try:

            Contact.objects.create(fullname=f, email=em, mobile=m, subject=s, message=msg,msgdate=date.today(),isread="no")
            error = "no"
        except:
            error = "yes"
    return render(request, 'contact.html', locals())

def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    contact = Contact.objects.filter(isread="no")
    return render(request,'unread_queries.html', locals())

def read_queries(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    contact = Contact.objects.filter(isread="yes")
    return render(request,'read_queries.html', locals())

def view_queries(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    contact = Contact.objects.get(id=pid)
    contact.isread = "yes"
    contact.save()
    return render(request,'views_queries.html', locals())


# class VideoForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         fields = ['video_file', 'description'] 

def blog(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    
    return  render(request,"blog.html")
#     error = ""
    
#     if request.method == 'POST':
       
#         d = request.POST.get('description')
#         v = request.FILES.get('video')
#         try:
            
#             b= Blog.objects.create(description=d, video=v)
#             # b.save()
#             error = "no"
#         except Exception as e:
#             print(e)  # Print the error for debugging purposes
#             error = "yes"

#     return render(request, 'blog.html', {'error': error})
  

def viewblogs(request):
    if request.method == 'POST':
        d = request.POST.get('description')
        v = request.FILES.get('video_file')
        #  if v:
        #      with open(os.path.join(settings.MEDIA_ROOT, v.name), 'wb') as video_file:
        #         for chunk in v.chunks():
        #             video_file.write(chunk)
            # with v.open() as video_file:
            #     video_content = v.read()
            #     video_file_instance = File(v, name=v.name)

        blog = Blog(description=d, video_file=v)
        blog.save()

        blogg = Blog.objects.all()
        return render(request, 'viewblogs.html', {"blogs": blogg})
       
    else:
        return  HttpResponse("Blog submitted unsuccessful")
    
     #  if v:
        #     video_content = v.read()
        #     blog=Blog(description=d, video_file=video_content)
        #     blog.save()
        #     blogg=Blog.objects.all()
        #     return render(request, 'viewblogs.html' , {"blogs":blogg} )
        # #  return  HttpResponse("Blog submitted successfully")
    # blogs = Blog.objects.all()
    # d = {'blogs': blogs}
   
    # return render(request, 'viewblogs.html', d)

def displayblog(request):
    blog=Blog.objects.all()
    return render(request, 'viewblogs.html' , {"blogs":blog} )

def teams(request):
    # team_members = Team.objects.all() 

    if request.method == 'POST':
        d = request.POST.get('description')
        image = request.FILES.get('image')
        # if image:
        team_member = Team(description=d, image=image)
        team_member.save()
        team_members = Team.objects.all()
        
        return render(request, 'teams.html', {"team_members":team_members})
    else:
        return  HttpResponse("Image submitted unsuccessful")
    
    # return render(request, 'teams.html', {"team_members":team_members})
  # Update team_members with the latest list of team members
        # else:
        #     return HttpResponse("Please select an image file to upload.")
    
        #  if v:
        #      with open(os.path.join(settings.MEDIA_ROOT, v.name), 'wb') as image:
        #         for chunk in v.chunks():
        #             image.write(chunk)
        #  if v:
        #     team_member = Team(description=d, image=v)
            # team_member.save()
           
        #      team_members = Team.objects.all()
        #      return render(request, 'teams.html', {"team_members": team_members})
        #  else:
        #      return HttpResponse("Please select an Image file to upload.")

def displayTeam(request):
    team=Team.objects.all().order_by('-id') 
    return render(request, 'teams.html' , {"team_members":team} )

def training(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    else:
        return  render(request,"training.html")

def view_training(request):

    if request.method == 'POST':
        d = request.POST.get('description')
        image = request.FILES.get('image')
        # if image:
        trainings = Team(description=d, image=image)
        trainings.save()
        trainingg = Team.objects.all()
        
        return render(request, 'viewtraining.html', {"trains":trainingg})
    else:
        return  HttpResponse("Training details submitted unsuccessful")
  
def displayTrainings(request):
    trainingg=Team.objects.all().order_by('-id') 
    return render(request, 'viewtraining.html' , {"trains":trainingg} )

def event_admin(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    else:
        return  render(request,"event_admin.html")
    
def view_event(request):

    if request.method == 'POST':
        image = request.FILES.get('image')
        l = request.POST.get('link')
        evt = Event( image=image, link=l)
        evt.save()
        events = Event.objects.all()
        
        return render(request, 'view_event.html', {"events":events})
    else:
        return  HttpResponse("Event submitted unsuccessful")
    
def displayEvent(request):
    event = Event.objects.all().order_by('-id') 
    return render(request, 'view_event.html', {"events":event})

