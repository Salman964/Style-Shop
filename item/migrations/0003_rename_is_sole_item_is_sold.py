# Generated by Django 4.2.8 on 2023-12-09 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='is_sole',
            new_name='is_sold',
        ),
    ]
