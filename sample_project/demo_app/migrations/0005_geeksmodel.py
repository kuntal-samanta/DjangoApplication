# Generated by Django 4.1.1 on 2022-09-18 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0004_securefiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
