# Generated by Django 4.1.2 on 2023-03-22 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0027_semester_routine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester',
            old_name='routine',
            new_name='final_routine',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='date',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='routine',
            name='teachers',
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('teachers', models.ManyToManyField(null=True, to='InvApp.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='routine',
            name='exams',
            field=models.ManyToManyField(null=True, to='InvApp.exam'),
        ),
    ]
