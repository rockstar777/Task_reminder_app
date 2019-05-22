# Generated by Django 2.2.1 on 2019-05-22 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0008_auto_20190520_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('notify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Task')),
            ],
        ),
    ]