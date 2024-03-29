# Generated by Django 4.2 on 2024-02-20 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_product_price_alter_productcomment_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('price', models.FloatField(verbose_name='price')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='store.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Price',
                'verbose_name_plural': 'Prices',
                'ordering': ['id'],
            },
        ),
    ]
