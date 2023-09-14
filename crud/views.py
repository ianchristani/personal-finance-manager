from django.shortcuts import render, redirect
from .models import eventModel
from .forms import eventForm

# logged in users page
def eventList(request):
    # colocar algum filtro de ordem de exibicao na proxima linha
    events = eventModel.objects.all()
    return render(request, "events.html", {"allEvents": events})

# adding a new event
def newEvent(request):
    newEventForm = eventForm(request.POST or None, request.FILES or None)
    # registering
    if newEventForm.is_valid():
        newEventForm.save()
        return redirect('crud:eventList')

    return render(request, 'event-form.html', {'eventform': newEventForm})

# event updater
def updateEvent(request, id):
    selectedEvent = eventModel.objects.get(id = id)
    neweventform = eventForm(request.POST or None, request.FILES or None, instance = selectedEvent)
    # updating
    if neweventform.is_valid():
        neweventform.save()
        return redirect('crud:eventList')
    
    return render(request, "event-form.html", {"eventform": neweventform, 'id': selectedEvent})

# event deleter
def deleteEvent(request, id):
    selectedEvent = eventModel.objects.get(id = id)
    # deleting
    if request.method == "POST":
        selectedEvent.delete()
        return redirect('crud:eventList')
    
    return render(request, 'event-delete-confirmation.html', {'eventtodelete': selectedEvent})