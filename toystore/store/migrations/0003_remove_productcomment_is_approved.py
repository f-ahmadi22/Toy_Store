# Generated by Django 4.2 on 2024-02-18 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_productmedia_productcomment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcomment',
            name='is_approved',
        ),
    ]
