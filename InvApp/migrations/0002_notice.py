# Generated by Django 4.1.2 on 2022-10-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=1000)),
                ('description', models.TextField(max_length=5000)),
            ],
        ),
    ]
