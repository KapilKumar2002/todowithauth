# Generated by Django 4.1 on 2022-11-27 08:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authapi', '0003_alter_userstodo_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstodo',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_todo', to=settings.AUTH_USER_MODEL),
        ),
    ]