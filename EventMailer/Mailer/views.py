from django.core.mail import send_mail
from .models import Event, EmailTemplate
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime



@api_view(['POST'])
def send_event_emails(request):
    current_date = datetime.date.today()
    events = Event.objects.filter(event_date=current_date)
    for event in events:
        try:
            template = get_object_or_404(EmailTemplate, event_type=event.event_type)
            employee = event.employee
            email_content = template.template_content.replace("{{employee_name}}",employee.name)
            send_mail(
                subject=f"Event Notification: {event.event_type}",
                message=email_content,
                from_email="sender_email_address",
                recipient_list=[employee.email],
                fail_silently=False,
                html_message=email_content,
            )

            # Log success
            event.sent_status = "Sent"
            event.save()

        except Exception as e:
            # Log error and continue
            event.sent_status = "Error: " + str(e)
            event.save()

    return Response({"message": "Event emails sent"})


