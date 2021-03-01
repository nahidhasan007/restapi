from rest_framework import generics,permissions

from blood_group.models import Location, Doner

# Create your views here.
from .serializers import LocationSerializer
from .serializers import DonerSerializer

class BloodAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class BloodCategoryAPIView(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Doner.objects.all()
    serializer_class = DonerSerializer

class BloodDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Doner.objects.all()
    serializer_class = DonerSerializer

class BloodNewView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Doner.objects.all().order_by('-id')[:1]
    serializer_class = DonerSerializer    
