# Generated by Django 5.1.6 on 2025-03-28 06:59

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='token_created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='verification_token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.DeleteModel(
            name='Issue',
        ),
    ]
