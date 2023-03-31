# Generated by Django 4.1.2 on 2022-10-17 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.PositiveBigIntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('batch', models.CharField(choices=[('f8', '48'), ('f7', '47'), ('f9', '49'), ('f0', '50')], default='f8', max_length=5)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('pwd', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.PositiveBigIntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('pwd', models.CharField(max_length=50)),
            ],
        ),
    ]