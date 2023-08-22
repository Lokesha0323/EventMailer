
from django.test import TestCase
from .models import Event, EmailTemplate, Employee
import datetime
from  django.test import Client
from django.urls import reverse

class EmailSystemTestCase(TestCase):
    def setUp(self):
        self.template = EmailTemplate.objects.create(event_type="Birthday", template_content="Happy birthday, {{employee_name}}!")
        self.employee = Employee.objects.create(name="John Doe", email="john@example.com")
        self.event = Event.objects.create(employee=self.employee, event_type="Birthday", event_date=datetime.date.today())

    def test_send_event_emails(self):
        client = Client()
        response = client.post(reverse('send-event-emails'),content_type='application/json')
        self.assertEqual(response.status_code, 200)
        event = Event.objects.get(id=self.event.id)
        self.assertEqual(event.sent_status, "Sent")

    def test_send_event_emails_error(self):
        self.template.delete()  # Delete the template to simulate an error
        client = Client()
        response = client.post(reverse('send-event-emails'),content_type='application/json')
        event = Event.objects.get(id=self.event.id)
        self.assertTrue(event.sent_status.startswith("Error:"))

