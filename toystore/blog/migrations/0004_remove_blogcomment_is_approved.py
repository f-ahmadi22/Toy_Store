# Generated by Django 4.2 on 2024-02-18 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_category_blogcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='is_approved',
        ),
    ]
