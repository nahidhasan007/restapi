from django.urls import path
from . import views
#from blood_group.views import AddDonerView

app_name = 'blood_group'
urlpatterns = [
 	 path('',views.index,name='index'),
 	 path('<int:location_id>/home',views.home,name='home'),
 	 path('search/',views.search,name='search'),
 	 path('add_location/',views.add_location,name='add_location'),
 	 path('add_doners/',views.AddDonerView.as_view(),name='add_doners'),
]