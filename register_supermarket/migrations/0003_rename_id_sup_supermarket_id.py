# Generated by Django 4.0.4 on 2022-04-22 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register_supermarket', '0002_remove_supermarket_id_alter_supermarket_id_sup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supermarket',
            old_name='id_sup',
            new_name='id',
        ),
    ]