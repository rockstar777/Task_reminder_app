# Generated by Django 2.2.1 on 2019-05-19 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190519_0628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='id',
            new_name='task_id',
        ),
    ]