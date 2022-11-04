from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
# Create your views here.

# rooms = [
#     {'id':1,'name':'lets learn python!'},
#     {'id':2,'name':'Design with me'},
#     {'id':3,'name':'Frontend developers'},
# ]


def home(request):
    rooms= Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'home.html',context)

def room(request, pk):
    # room= None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room= Room.objects.get(id= pk)
    context = {'room':room}        
    return render(request, 'room.html',context)


def createRoom(request):
    form = RoomForm() #have a form
    if request.method == 'POST': #send the post data
        form = RoomForm(request.POST) #add the data to the form
        if form.is_valid(): #check if the data is valid
            form.save() # if it is good we save it
            return redirect('home') #then we redirect the user
    context = {'form':form}
    return render(request, 'room_form.html',context)



def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance= room) #add the data to the form

    if request.method == 'POST':
        form = RoomForm(request.POST, instance= room)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form':form}
    return render(request, 'room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id= pk)
    if request.method == 'POST':
        room.delete
    return render(request, 'delete.html', {'obj':room})