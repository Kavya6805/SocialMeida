# Generated by Django 4.0.3 on 2024-09-14 04:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('follower', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('follower', 'user')},
        ),
    ]
