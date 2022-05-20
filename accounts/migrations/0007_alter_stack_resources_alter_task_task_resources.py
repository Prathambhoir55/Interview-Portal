# Generated by Django 4.0.3 on 2022-05-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_task_task_resources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stack',
            name='resources',
            field=models.FileField(blank=True, max_length=200, upload_to='resources'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_resources',
            field=models.FileField(blank=True, upload_to='tasks'),
        ),
    ]