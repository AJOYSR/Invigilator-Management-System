# Generated by Django 4.1.1 on 2023-03-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0045_exam_exam_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='registration_number',
            field=models.PositiveBigIntegerField(unique=True),
        ),
    ]
