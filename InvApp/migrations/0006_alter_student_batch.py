# Generated by Django 4.1.2 on 2022-10-19 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0005_teacher_short_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='batch',
            field=models.CharField(blank=True, choices=[('48', '48'), ('47', '47'), ('49', '49'), ('50', '50')], default='48', max_length=30, null=True),
        ),
    ]
