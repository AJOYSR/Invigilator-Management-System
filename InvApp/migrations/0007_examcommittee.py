# Generated by Django 4.1.2 on 2022-10-19 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0006_alter_student_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCommittee',
            fields=[
                ('teacher_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='InvApp.teacher')),
                ('is_chairman', models.CharField(choices=[{'KaderMia-', None}], max_length=100, null=True)),
            ],
            bases=('InvApp.teacher',),
        ),
    ]