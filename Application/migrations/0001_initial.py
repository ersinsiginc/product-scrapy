# Generated by Django 3.1.6 on 2022-07-04 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MerchantInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=160, null=True)),
                ('city_name', models.CharField(blank=True, max_length=160, null=True)),
                ('seller_score', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=160, null=True)),
                ('brand', models.CharField(blank=True, max_length=160, null=True)),
                ('selling_price', models.FloatField(blank=True, null=True)),
                ('discounted_price', models.FloatField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=160, null=True)),
                ('merchant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Application.merchantinfo')),
            ],
        ),
    ]
