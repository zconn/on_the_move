from django.shortcuts import render
from django.http import HttpResponse

def step_tracker_main(request):
    #return HttpResponse("Testing Step Tracker Page. Working!")
    return render(request, 'step_tracker/step_entry.html')