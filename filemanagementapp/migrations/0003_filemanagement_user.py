# Generated by Django 3.2.6 on 2021-11-27 01:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filemanagementapp', '0002_alter_filemanagement_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='filemanagement',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
