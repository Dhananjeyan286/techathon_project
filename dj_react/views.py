from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import user
from random import randint
from django.core.mail import send_mail
from passlib.hash import pbkdf2_sha256
from django.contrib import messages
import json
# Create your views here.


def start(request):
    return render(request,"index.html")
def signup(request):
    if request.method == 'POST':
        email_id = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        name = request.POST.get("name")
        hash_pass = pbkdf2_sha256.hash(password)
        new_user = user(email_id,name,hash_pass,False,False,True)
        
        new_user.save()
        return JsonResponse({"success":True})
def signin(request):
    if request.method == 'POST' and request.is_ajax():
        result = False
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        obj = user.objects.get(email_id=email)
        
        db_pass = obj.password
        
        if pbkdf2_sha256.verify(password,db_pass):
            
            result = True
            request.session['email']=email
        if result==True:
            print("valid backend")
        print(result)
        return JsonResponse({"redirect":str(result)})
    
def signin_redirect(request):
    email = request.session.get('email')
    obj = user.objects.get(email_id = email)
    is_admin = obj.admin
    return render(request,"homepage.html",{"user":obj,"is_admin":is_admin})
def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        obj = user.objects.filter(email_id = email)
        if obj.exists():
            request.session["email"]=email
            otp=str()
            
            for i in range(6):
                otp = otp+str(randint(0,9))
            head = "otp verification"
            fro = "eshwaran2001@gmail.com"
            body = "the otp for change of password is "+otp
            request.session['otp']=otp
            send_mail(head,body,fro,[email],fail_silently=False)
            return JsonResponse({"result":"True"})
        else :
            return JsonResponse({"result":"False"})

    
def forgot_pass(request):
    return render(request,'changepassword.html')
def validate_otp(request):
    result = False
    if request.method == 'POST':
        otp = request.POST.get("otp")
        check_otp = request.session.get('otp')
       
       
        if otp==check_otp:
            result = True
        
    return JsonResponse({"result": str(result)})
def request_changepass(request):
    
    return render(request,'enterpassword.html')
def new_pass(request):
    if request.method == 'POST':

        password = request.POST['password']
        con_password = request.POST['confirmpassword']
        if not(password):
            messages.error(request,"enter the password")
            return redirect('/request_changepass')
            
        elif not(con_password):
            messages.error(request,'enter the confirm password')
            return redirect('/request_changepass')
            
        elif password != con_password:
            messages.error(request,'password and confirm password do not match')
            return redirect('/request_changepass')
            
        
        email = request.session.get("email")
        obj = user.objects.get(email_id = email)
        if obj:
            passwd = pbkdf2_sha256.hash(password)
            obj.password = passwd
            obj.save()
        else:
            return render(request,'enterpassword.html')
        
        return render(request,'index.html')

def home_page(request):
    return render(request,"homepage.html")
def user_details(request):
    
    obj = user.objects.all()
    
    return render(request,'listofusers.html',{"users":obj})
def logout(request):
    print('hi')
    try:
        del request.session['email']
    except KeyError:
        pass
    messages.error(request,'you are logged out successfully')
    return render(request,'index.html')
def change(request):
    email = request.POST['email']
    type_user = request.POST.get('type1',False)
    request.session['change_user']=email
    request.session['change_type']=type_user
    print(type_user)
    print(email)
    if type_user=='normal':
        messages.error(request,'do you wanna change this user to premium user')
        return redirect('/users_details')
    else:
        messages.error(request,'do you wanna change this user to normal user')
        return redirect('/users_details')
def change_user(request):
    email = request.session.get('change_user')
    type_user = request.session.get('change_type')
    obj = user.objects.get(email_id = email)
    if type_user == 'normal':
        obj.premium = True
        obj.normal = False
    else:
        obj.normal = True
        obj.premium = False
    obj.save()
    return redirect('/users_details')
def decline_user(request):
    try:
        del request.session['change_user']
        del request.session['change_type']
    except:
        pass
    return redirect('/users_details')


    

        
    
