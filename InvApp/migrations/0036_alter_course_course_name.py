# Generated by Django 4.1.1 on 2023-03-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0035_alter_exam_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=200),
        ),
    ]
