# Generated by Django 4.2.4 on 2023-08-22 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Mailer", "0002_event_event_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="event_status",
            new_name="sent_status",
        ),
    ]
