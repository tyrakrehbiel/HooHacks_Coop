# Generated by Django 3.0.4 on 2020-03-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default="I'm ready to learn!", max_length=500),
        ),
    ]
