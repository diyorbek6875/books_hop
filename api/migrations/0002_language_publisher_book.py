# Generated by Django 4.2.7 on 2023-11-11 10:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(limit_value=0.0)])),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0)])),
                ('isbn', models.IntegerField()),
                ('pages', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0)])),
                ('pubished_date', models.DateField()),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.language')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.publisher')),
            ],
        ),
    ]
