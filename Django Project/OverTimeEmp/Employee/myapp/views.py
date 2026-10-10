from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def main(request):
    shift = Shift.objects.all()
    return render(request, 'index.html', {'shift' :shift})

def add(request):

    if request.method == 'POST':

        name = request.POST['name']
        role = request.POST['role']
        employee_id = request.POST['employee_id']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']

        value = Employee(name = name, role = role)

        value.save()

        shiftValue = Shift(emp = value, employee_id = employee_id, start_time = start_time, end_time = end_time )

        shiftValue.save()

        return redirect('main')

    return render(request, 'add.html')


def delete(request,id):
    shift = Shift.objects.get(id=id)
    shift.delete()
    return redirect('main')

def update(request,id):
    shift = Shift.objects.get(id=id)

    emp = shift.emp

    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        employee_id = request.POST['employee_id']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']

        emp.name = name 
        emp.role = role

        emp.save()

        shift.employee_id = employee_id
        shift.start_time = start_time
        shift.end_time = end_time

        shift.save()
        

        return redirect('main')

    return render(request, 'update.html', {'shift' : shift})