# Generated by Django 4.2.4 on 2023-08-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Mailer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="event_status",
            field=models.CharField(default="sent", max_length=10),
            preserve_default=False,
        ),
    ]
