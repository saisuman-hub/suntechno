from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Userinfo , Booking_info
from django.contrib import messages
#from django.contrib.auth.models import User,auth

# Create your views here.
def demo(request):
    return render(request,'hotels/main.html')

def regisinfo1(request):
    return render(request,'hotels/register.html')

def regisinfo(request):
    if request.method == 'POST':
        first = request.POST['firstname'] 
        last = request.POST['lastname']    
        user = request.POST['username']    
        email = request.POST['emailid']    
        passs = request.POST['password']    
        reent = request.POST['re_enter'] 
        if passs == reent:
            if Userinfo.objects.filter(username=user).exists():
                messages.info(request,'This username has already used')
                return redirect('register')
            elif Userinfo.objects.filter(email_id=email).exists():
                messages.info(request,'email exist please choose another one')
                return redirect('register')
            else:    
                info_fo = Userinfo(firstname=first,lastname=last,username=user,email_id=email,password=passs,re_enter=reent)
                info_fo.save()
                return HttpResponse('sucessfully register')
        else:
            messages.info(request, 'Password did not matched')   
            return redirect('register')
        return redirect('/')    
    return render(request, 'hotels/register.html')

    
def verifycred(request):
    if request.method == 'POST':
        user1 = request.POST['username']    
        pass1 = request.POST['password']
        try:
            info_fo = Userinfo.objects.get(username=user1,password=pass1)    
            return render(request, 'hotels/logout.html')

        except Userinfo.DoesNotExist:
            messages.info(request, 'invalid crendentials')
            return redirect('/')

    else:
         return render(request, 'hotels/main.html')

def booking(request):
    bhk2 = None
    if request.method == 'POST':
        ch = request.POST['checkin']
        ch1 = request.POST['checkout']
        bhk = request.POST['bhk']
        if bhk:
            bhk2 = False
        else:
            bhk2 = True
        
        book = Booking_info(checkin=ch,checkout=ch1,singleBHK=bhk,doubleBHK=bhk2)  
        book.save()
        return render(request,'hotels/search.html')

def forget(request):
    return render(request,'hotels/forget.html')

def mail_retrive(request):
    em = request.POST['email'] 
    mail = Userinfo.objects.get(email_id=em) 
    print(mail.password) 
    return HttpResponse(mail.password) 

    

      
        
   


