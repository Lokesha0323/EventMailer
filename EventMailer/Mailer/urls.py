from django.urls import path
from . import views

urlpatterns = [
    path('send-event-emails/', views.send_event_emails, name='send-event-emails'),
    # Define other API endpoints here
]
