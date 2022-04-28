# Generated by Django 4.0.4 on 2022-04-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=11, blank=False)),
                ('address', models.TextField()),
                ('balance', models.PositiveIntegerField(default=20000, null=True)),
                ('city', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=20)),
            ],
            # should ask:
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]