# Generated by Django 4.1.1 on 2022-10-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0016_remove_semester_examcommittee_examcommittee_semester_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examcommittee',
            name='teacher',
        ),
        migrations.AddField(
            model_name='examcommittee',
            name='teacher',
            field=models.ManyToManyField(to='InvApp.teacher'),
        ),
    ]
