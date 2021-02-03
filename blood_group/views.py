from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from . models import Location, Doner
from django.views.generic import CreateView

# Create your views here.
def index(request):
	areas = Location.objects.all()
	return render(request,'blood_group/index.html',{'areas':areas})

def add_location(request):
	if request.method=="POST":
		location_name = request.POST['location_name']
		loc = Location(location_name=location_name)
		loc.save();
		return render(request,'blood_group/index.html')

	else:
		return render(request,'blood_group/add_location.html')
		
class AddDonerView(CreateView):
	model = Doner
	template_name = 'blood_group/add_doners.html'
	fields = '__all__'

def home(request, location_id):
	loc = Location.objects.get(pk=location_id)
	data = loc.doner_set.all()
	return render(request,'blood_group/home.html',{'data':data,'loc':loc})

def search(request):
	query = request.GET.get('give')
	data = Doner.objects.filter(donar_blood_group=query)
	return render(request,'blood_group/search.html',{'data':data})




