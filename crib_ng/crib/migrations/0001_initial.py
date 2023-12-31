# Generated by Django 4.2.3 on 2023-08-02 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('date_added', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_sold', models.DateTimeField(verbose_name='time sold')),
                ('quantity_sold', models.IntegerField(default=0)),
                ('product_sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crib.products')),
            ],
        ),
    ]
