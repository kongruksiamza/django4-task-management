from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    #ส่งข้อมูลจากฟอร์ม
    if request.method=="POST":
        #รับค่า
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        #ตรวจสอบว่าเป็นค่าว่างหรือไม่
        if username == "" or password == "" or repassword == "":
            messages.warning(request,"กรุณาป้อนข้อมูลให้ครบ")
            return redirect("/register")
        else :
            #รหัสผ่านตรงกันหรือไม่
            if password == repassword:
                #ตรวจสอบชื่อบัญชีว่าซ้ำหรือไม่
                if User.objects.filter(username=username).exists():
                    messages.warning(request,"Username นี้มีคนใช้งานแล้ว")
                    return redirect("/register")
                #สร้างบัญชีผู้ใช้
                else:
                    user=User.objects.create_user(
                        username=username,
                        password=password
                    )
                    user.save()
                    messages.success(request,"สร้างบัญชีผู้ใช้เรียบร้อย")
                    return redirect("/register")
            else:
                messages.warning(request,"รหัสผ่านไม่ตรงกัน")
                return redirect("/register")
    else :
        return render(request,"register.html")

def login(request):
    if request.method == "POST":
        #รับค่าจากแบบฟอร์ม
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "" or password == "":
            messages.warning(request,"กรุณาป้อนข้อมูลให้ครบ")
            return redirect("/login")
        else :
            #ตรวจสอบการเข้าสู่ระบบ
            user=auth.authenticate(username=username,password=password)
            #มีข้อมูลในระบบ
            if user is not None :
                auth.login(request,user)
                return redirect("/")
            else :
                messages.warning(request,"ไม่มีบัญชีนี้ในระบบ")
                return redirect("/login")      
    else :
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/login")