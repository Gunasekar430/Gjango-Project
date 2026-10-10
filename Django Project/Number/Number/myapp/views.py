from django.shortcuts import render
from .models import *

def main(request):

    if request.method == 'POST':

        Mark = request.POST.get('mark')
        Time = request.POST.get('time')

        print("Mark:", Mark)
        print("Time:", Time)

        numbers = number(
            mark=Mark,
            time=Time
        )

        numbers.save()

        return render(
            request,
            'index.html',
            {'numbers': numbers}
        )

    return render(request, 'index.html')