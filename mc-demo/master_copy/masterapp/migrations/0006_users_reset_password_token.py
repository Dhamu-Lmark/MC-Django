# Generated by Django 5.0.3 on 2024-03-25 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masterapp', '0005_contactsubmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='reset_password_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
