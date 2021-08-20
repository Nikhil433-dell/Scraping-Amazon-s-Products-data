# Generated by Django 3.2.5 on 2021-08-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=10)),
                ('desc', models.TextField()),
                ('stock', models.CharField(max_length=50)),
            ],
        ),
    ]