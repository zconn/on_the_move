from django.shortcuts import render
from django.http import HttpResponse

def step_tracker_main(request):

    if request.method == "POST":
        if request.POST.get("entry_type") == 'activity':
            print(request.POST.get("activity"))
            print(request.POST.get("duration"))
        print(request.POST.get("steps"))
    return render(request, 'step_tracker/step_entry.html')