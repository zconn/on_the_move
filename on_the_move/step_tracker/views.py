from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from step_tracker.models import Steps

def step_tracker_main(request):

    if request.method == "POST":
        print(type(request.POST))
        for x in request.POST:
            print(x)
        # print("User1")
        # print(request.POST.get("date"))
        # print(request.POST.get("steps"))
        # if request.POST.get("entry_type") == 'activity':
        #     print(request.POST.get("activity"))
        #     print(request.POST.get("duration"))
        steps_entry = Steps(author=request.user, entry_date=request.POST.get("date"), steps=request.POST.get("steps"))
        steps_entry.save()
    steps_today = Steps.objects.filter(author=request.user, entry_date=datetime.today()).aggregate(steps=Sum("steps"))
    context = {'steps_today':steps_today['steps']}
    return render(request, 'step_tracker/step_entry.html', context)