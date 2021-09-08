from django.urls import path
from events.views import *


urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('event_detail/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event_create/', EventCreateView.as_view(), name='event_create'),
    path('event_edit/<int:pk>/', EventEditView.as_view(), name='event_edit'),
    path('ware_list/', WarehouseEvent.as_view(), name='ware_list'),

]