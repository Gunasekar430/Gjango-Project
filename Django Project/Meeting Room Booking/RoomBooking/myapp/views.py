from django.shortcuts import redirect, render
from .models import *
# Create your views here.

def main(request):
    room = Room.objects.all()
    return render(request, 'index.html', {'room' : room})

def addRoom(request):
    # room = Room.objects.all()

    if request.method == 'POST':
        room_name = request.POST['room_name']
        capacity = request.POST['capacity']
        location = request.POST['location']

        room = Room(room_name = room_name, capacity = capacity, location = location)
        room.save()

        return redirect('main')

    return render(request, 'addRoom.html')

def bookingRoom(request,id):
    room = Room.objects.get(id = id)

    if request.method == 'POST':
        title = request.POST['title']
        start_Time = request.POST['start_Time']
        end_Time = request.POST['end_Time']
        booked_by = request.POST['booked_by']

        meeting = Meeting(room = room, title = title, end_Time = end_Time, start_Time = start_Time, booked_by = booked_by)

        meeting.save()

        return redirect('main')
    
    return render(request, 'bookingRoom.html', {'room' : room})

def viewBooking(request):
    meeting = Meeting.objects.all()
    return render(request, 'viewBooking.html', {'meeting' : meeting})

def cancel(request, id):
    meeting = Meeting.objects.get(id = id)
    meeting.delete()

    return redirect('viewBooking')