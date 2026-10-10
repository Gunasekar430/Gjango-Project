from django.shortcuts import redirect, render
from .models import *
# Create your views here.


def main(request):
    Shift = ShiftList.objects.all()
    return render(request, 'index.html', {"Shift" : Shift})

def delete(request, id):
    delete = ShiftList.objects.get(id=id)
    delete.delete()
    return redirect('main')

def add(request):
    if request.method == "POST":
        a = request.POST["name"]
        b = request.POST["role"]
        c = request.POST["startTime"]
        d = request.POST["endTime"]

        emp = EmployeeList(Name = a, Role = b)
        emp.save()

        shift = ShiftList(employee = emp, StartTime = c, EndTime = d)
        shift.save()

        return redirect('main')
    return render(request, "add.html")


def view(request, id):
    view = ShiftList.objects.get(id=id)
    return render(request, 'view.html', {"view" : view})

def update(request, id):
    update = ShiftList.objects.get(id=id)

    if request.method == "POST":
        a = request.POST['name']
        b = request.POST['role']
        c = request.POST['startTime']
        d = request.POST['endTime']
        
        emp = update.employee

        emp.Name = a 
        emp.Role = b

        emp.save()

        update.StartTime = c
        update.EndTime = d

        update.save()
        
        return redirect('main')
    return render(request, 'update.html', {"update" : update})