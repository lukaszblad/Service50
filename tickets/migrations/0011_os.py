# Generated by Django 5.0.3 on 2024-04-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('specification', models.CharField(max_length=64)),
            ],
        ),
    ]
