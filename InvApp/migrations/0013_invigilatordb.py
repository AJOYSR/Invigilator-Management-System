# Generated by Django 4.1.1 on 2022-10-26 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0012_alter_examcommittee_is_chairman_semester'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvigilatorDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InvApp.semester')),
            ],
        ),
    ]