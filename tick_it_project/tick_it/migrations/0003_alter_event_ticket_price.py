# Generated by Django 4.2.3 on 2023-07-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tick_it', '0002_alter_event_event_date_alter_event_event_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ticket_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
