from asyncio import events
from ctypes import addressof
import http
import re
from statistics import mode
from urllib import response
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from multiprocessing import context
from pyexpat import model
from typing import Counter
from django.shortcuts import render
from django.core.mail import send_mail
import hashlib,random,os

import fpdf
from . import models
from datetime import date
from django.core.mail import EmailMessage
from fpdf import FPDF
from django.core.mail import EmailMessage


# Create your views here.



ordcounter = 1
evcounter = 1


def bookingfetch(request):
    count=0
    al_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    event_list = models.Event.objects.all()
    istr = ''' '''
    for event in event_list:
        
        istr += '''
                    <style>
                    #a-'''+str(event.id)+'''{
                        width: 80px;
                    }
                    </style>
                    <section class="kp">
                    <pre class="rrr">
                <u>Event</u>                              <u>Teams</u>                         <u>Time</u>                              <u>Place </u>                          <u>Date </u>                         <u>Seats remaining</u>                   <u>Number of seats</u>                                    

                        
        '''+event.E_name+'                      '+event.E_teams+'                    '+str(event.E_time)+'                          '+event.E_location+'                     '+str(event.E_date)+'                          '+str(event.E_seat)+'''                                   <button id="%ssab">-</button>  <input type="number" id=a-'''% (al_list[count])+str(event.id)+ ''' readonly="" value="0">  <button id="%sad">+</button>         <button class="button button1" id="%sbk" onclick=ord(''' %(al_list[count],al_list[count])+str(event.id)+''') >BOOK</button>
                                                                                                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                 
                        </pre>
                        </section >
                        <br>
                        <br>
                        <script type="text/javascript">
                            let %saddB = document.querySelector('#%sad');
                            let %ssubB = document.querySelector('#%ssab');
                            let %sqtyn = document.querySelector('#a-'''% (al_list[count],al_list[count],al_list[count],al_list[count],al_list[count])+str(event.id)+'''');
                            let %sbg = document.querySelector('#%sbk');
                                                                                                                                                                                                                                              
                            %saddB.addEventListener('click',()=>{
                            %sqtyn.value = parseInt(%sqtyn.value) + 1;
                        });
                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                            
                        %ssubB.addEventListener('click',()=>{
                            if (%sqtyn.value <= 0) {
                                %sqtyn.value = 0;
                            }
                            else{
                                %sqtyn.value = parseInt(%sqtyn.value) - 1;
                                }
                            });
                                                                                                                                                                                                                                             
                        </script>
                        ''' % (al_list[count],al_list[count],al_list[count],al_list[count],al_list[count],al_list[count],al_list[count],al_list[count],al_list[count],al_list[count])+'''
                       '''
        count+=1
    # print(istr)
    return HttpResponse(istr)
    
    

def fetchall(request):
    event_list = models.Event.objects.all()
    istr = ''' '''
    for event in event_list:
        istr += '''        <section class="kp">
                              <pre class="rrr">
                                             <b>  <u>Event</u>  </b>                         <b> <u>Teams</u> </b>                   <b> <u>Time</u> </b>             <b>  <u>Place</u> </b>                    <b> <u>Date</u> </b>             <b>  <u>Total seats remaining </u> </b>
                                                            
                            '''+event.E_name+'               '+event.E_teams+'                '+str(event.E_time)+'                  '+event.E_location+'                  '+str(event.E_date)+'                           '+str(event.E_seat)\
                            +'''</pre>
                                </section>
                                <br>
                                '''
    print(istr)
    return HttpResponse(istr)


# event registration
def ereg(request):
    global evcounter
    pdf = FPDF()
    fname = request.GET.get('fname')
    mail = request.GET.get('mail')
    # phone = request.GET.get('num')
    subject = request.GET.get('subject')
    print(f"{fname},{mail},{subject}")
    c = models.EventReg(name=fname,email=mail,details=subject)
    c.save()
    dmail = request.GET.get('mail')
    g = models.EventReg.objects.get(email=dmail)
    gmail = g.email
    fname = g.name
    descrip = g.details
    print(f"THE MAIL {gmail},{fname},{descrip}")
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(0, 10, txt = "Shimoga Sports Club", ln = 1, align = 'C')
    pdf.cell(200, 10, txt = f"Order Invoice #{evcounter}.", ln = 2, align = 'C')
    pdf.cell(0, 10, txt = f"Your ID               : {g.id}", ln = 2, align = 'L')
    pdf.cell(0, 10, txt = f"Full Name               : {fname}", ln = 2, align = 'L')
    pdf.cell(0, 10, txt = f"Email               : {gmail}", ln = 2, align = 'L')
    pdf.cell(0, 10, txt = f"Event Details:", ln = 2, align = 'L')
    pdf.multi_cell(0, 10, txt = f"{descrip}",border=1, align = 'L')
    pdf.output("./Order_logs/EV_order"+str(evcounter)+".pdf")
    msg = EmailMessage('Event Order Invoice #'+str(evcounter), 'Thank you for booking! \nOur team will reach out to you! \n Your Event order Invoice is in the pdf. ', 'shimogasportsclub@gmail.com', [gmail])
    msg.content_subtype = "html"  
    msg.attach_file('./Order_logs/EV_order'+str(evcounter)+'.pdf')
    msg.send()
    print(f"The counter {evcounter}")
    evcounter += 1
    return HttpResponse("Email has been sent check your Invoice!")


    

def ureg(request):
    uname = request.GET.get('usrname')
    pwd = request.GET.get('psw')
    pwd = hashlib.md5(pwd.encode('utf-8')).hexdigest()

    email = request.GET.get('email')
    address = request.GET.get('address')
    number = request.GET.get('number')
    print(uname,pwd,email,address,number)
    g = models.Customer.objects.filter(C_mail = email)
    if g:
        return HttpResponse("user exists")
    u = models.Customer(C_name=uname,C_password=pwd,C_phone=number,C_address=address,C_mail=email)
    u.save()
    u=models.Customer.objects.get(C_mail = email)
    res = send_mail("Regsitration", "Congratulations!. Your registration is successfull and your customer id is "+str(u.id)+" Thank you for choosing our service", "shimogasportsclub@gmail.com", [email])
    return render(request,'login.html')

def loginpath(request):
    return render(request,'login.html')

def ulogin(request):
    email = request.GET.get('email')
    pwd = request.GET.get('psw')
    pwd = hashlib.md5(pwd.encode('utf-8')).hexdigest()
    print(email,pwd)
    u = models.Customer.objects.filter(C_mail=email,C_password=pwd)
    if(u):
        print(f"THE USER USED THE LOGIN EMAIL ID AS {email}")
        response = render(request,'home.html')
        response.set_cookie('email',email)
        test = request.COOKIES.get('email')
        print(f"cookie {test}")
        return response
    else:
        print(f"[ERROR]: THE USER FAILED {email}")
        return HttpResponse("failed")

def registerpath(request):
    return render(request,'register.html')

def aboutus(request):
    return render(request,'aboutus.html')

def contactpath(request):
    return render(request,'contactus.html')

def homepath(request):
    return render(request,'home.html')

def eventspath(request):
    return render(request,'events.html')

def bookingpath(request):
    return render(request,'booking.html')


def pushupdate(email,ono,value):
    e = models.Event.objects.get(id = ono)
    e.E_seat = e.E_seat - int(value)
    e.save()
    
    

def uorder(request):
    pdf = FPDF()
    global ordcounter
    email = request.COOKIES.get('email')
    ono = request.GET.get('ono')
    value = request.GET.get('number')
    print(f"this is number of seats booked  {value}")
    print(email)
    d = models.Customer.objects.get(C_mail = email)
    e = models.Event.objects.get(id = ono)
    d.BOOK.add(e)
    today = date.today()
    b = models.BOOK(T_date=today,No_seats = value,Cust_id =d.id ,EV_id = ono)
    b.save()
    pushupdate(email,ono,value)

    c=models.Customer.objects.get(C_mail=email)
    email=c.C_mail
    print(f"THIS IS USER MAIL ID {email}")
    m=models.Event.objects.get(id=ono)
    ename=m.E_name
    eteams = m.E_teams
    edate = m.E_date
    etime = m.E_time
    eloc = m.E_location
    eprice = m.E_price * int(value)
    eseats = value
    print(f"The user details {c.id}")
    print(f"THIS IS EVENT {ename},{eteams},{edate},{etime},{eloc},{eprice},{eseats}")
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    pdf.cell(0, 10, txt = "Shimoga Sports Club", ln = 1, align = 'C')
    pdf.cell(200, 10, txt = f"Order Invoice #{ordcounter}.", ln = 2, align = 'C')
    data = f"""
    Your ID               : {c.id}
    Event                  : {ename}
    Teams                 : {eteams}
    Date                   : {edate}
    Time                   : {etime}
    Location              : {eloc}
    Price                  : {eprice}
    Number of Seats booked : {eseats}"""
    pdf.multi_cell(0, 10, txt = data,border=1, align = 'L')
    pdf.output("./Order_logs/Order"+str(ordcounter)+".pdf")
    msg = EmailMessage('Order Invoice #'+str(ordcounter), 'Thank you for booking! \nYour order Invoice is in the pdf. ', 'shimogasportsclub@gmail.com', [email])
    msg.content_subtype = "html"  
    msg.attach_file('./Order_logs/Order'+str(ordcounter)+'.pdf')
    msg.send()
    print(f"The counter {ordcounter}")
    ordcounter += 1
    return HttpResponse("THANK YOU FOR BOOKING! check your Inbox for Invoice!")





def sendSimpleEmail(request):
   res = send_mail("Hello,", "Hope you are doing fine", "shimogasportsclub@gmail.com", ["gowdaarjun555@gmail.com"])
   return HttpResponse('%s'%res)


# OTP
def getotp(request):
    otp = random.randint(000000,999999) 
    email=request.GET.get('email') 
    file_exists = os.path.exists('enm.txt')
    ss=''
    if file_exists:
        f = open("enm.txt", "r")
        for fh in f:
            s=fh.split(":")
            em=s[0]
            if em==email:
                continue
            s+=fh
        f.close()        
    f = open("enm.txt", "w")
    ss+=email+":"+str(otp)
    f.write(ss)
    f.close()
    send_mail("OTP", "Your OTP is "+str(otp), "shimogasportsclub@gmail.com", [email])
    return HttpResponse('Mail sent')


def cpass(request):
    return render(request,"cpass.html")


def changepass(request):
    email=request.GET.get('email') 
    rotp=request.GET.get('rotp') 
    npsw=request.GET.get('npsw') 
    f = open("enm.txt", "r")
    for fh in f:
        s=fh.split(":")
        em=s[0]
        otp=s[1]
        if em==email and otp==rotp :
                c=models.Customer.objects.get(C_mail=email)
                npsw=hashlib.md5(npsw.encode('utf-8')).hexdigest()
                c.C_password=npsw
                c.save()

                return HttpResponse("Password changed successfully")
    return HttpResponse("OTP invalid")

