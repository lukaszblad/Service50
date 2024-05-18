# Generated by Django 5.0.3 on 2024-04-06 17:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_os'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration_Item',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=32)),
                ('model', models.CharField(max_length=32)),
                ('operating_system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.os')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]