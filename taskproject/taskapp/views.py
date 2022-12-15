from django.shortcuts import render,redirect
from django.http import HttpResponse
from taskapp.models import Task
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def index(request):
    if request.method == "POST":
        #ดึงข้อมูลจากฟอร์ม
        name = request.POST["name"]
        #เช็คค่าว่าง
        if name == "":
            #ส่งข้อความแจ้งเตือนผู้ใช้
            messages.warning(request,"กรุณาป้อนชื่อรายการ")
            return redirect("/")
        else :
            #บันทึกข้อมูล
            task=Task.objects.create(name=name,manager=request.user)
            task.save()
            messages.success(request,"บันทึกข้อมูลเรียบร้อย")
            return redirect("/")
    else :
        all_task = Task.objects.filter(manager=request.user)
        #ระบบหมายเลขหน้า
        page = request.GET.get("page")
        paginator = Paginator(all_task,4)
        all_task = paginator.get_page(page)

        return render(request,"index.html",{"all_task":all_task})

@login_required(login_url="/login")
def complete_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    if task.manager == request.user:
        task.status=True
        task.save()
        return redirect('/')
    else:
        messages.warning(request,"คุณไม่มีสิทธิ์เปลี่ยนสถานะ")
        return redirect("/")

@login_required(login_url="/login")
def pending_task(request,task_id):
    task = Task.objects.get(pk=task_id)
    if task.manager == request.user:
        task.status=False
        task.save()
        return redirect('/')
    else :
        messages.warning(request,"คุณไม่มีสิทธิ์เปลี่ยนสถานะ")
        return redirect("/")