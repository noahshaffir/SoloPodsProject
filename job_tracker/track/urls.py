from django.urls import path

from . import views
from track.views import ApplicationListView,SpecificApplicationView
app_name = 'track'
urlpatterns = [
    path('index/', views.ApplicationListView.as_view(), name='index'),
    path('detail/',views.SpecificApplicationView.as_view(),name='detail'),
]