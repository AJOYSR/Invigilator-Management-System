# Generated by Django 4.1.1 on 2023-03-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvApp', '0040_alter_notice_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='notice_images'),
        ),
    ]