# Generated by Django 5.1.1 on 2024-10-03 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elonlar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='announcements/'),
        ),
    ]
