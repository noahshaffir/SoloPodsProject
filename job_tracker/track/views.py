from datetime import timezone
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from track.models import *
# Create your views here.
class ApplicationListView(ListView):
    model = Application
    template_name = 'track/index.html'
    context_object_name = 'latest_application_list'
    def get_queryset(self):
        
        return Application.objects.filter().order_by('-date_applied')