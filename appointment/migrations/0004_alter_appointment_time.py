# Generated by Django 4.2.6 on 2024-01-12 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_alter_review_rating'),
        ('appointment', '0003_remove_appointment_time_appointment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.availabletime'),
        ),
    ]
