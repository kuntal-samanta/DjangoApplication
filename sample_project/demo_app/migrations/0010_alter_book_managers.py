# Generated by Django 4.1.1 on 2022-09-21 18:45

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0009_book'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('book_create_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]