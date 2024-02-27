# Generated by Django 4.2 on 2024-02-17 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('media_type', models.CharField(choices=[('image', 'image'), ('video', 'video')], max_length=20, verbose_name='media_type')),
                ('media_file', models.FileField(upload_to='media/store/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media', to='store.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'ProductMedia',
                'verbose_name_plural': 'ProductMedia',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('author', models.CharField(max_length=250, verbose_name='author')),
                ('content', models.TextField(verbose_name='content')),
                ('is_approved', models.BooleanField(default=False, verbose_name='is_approved')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='store.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'ProductComment',
                'verbose_name_plural': 'ProductComments',
                'ordering': ['id'],
            },
        ),
    ]
