# Generated by Django 3.2.12 on 2022-02-17 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20220217_0834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedulemeetingdata',
            old_name='timeslot',
            new_name='schedule',
        ),
    ]
