from rest_framework import generics   
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Event
from Serializers import EventSerializer

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

@api_view(['GET'])
def getEvents(request):
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
def addEvent(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET','PUT'])
def updateEvent(request , id= None):
    event = Event.objects.get(id=id)
    serializer = EventSerializer(instance=events, sata=request.data)
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201-CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteEvent(request, id=None):
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response(status="Event not found")
    
    event.delete()
    return Response(status="Event deleted")

            
            
