# Generated by Django 5.1.2 on 2024-10-26 07:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('availability_status', models.BooleanField(default=True)),
                ('edition', models.CharField(blank=True, max_length=100, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
