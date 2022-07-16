# Generated by Django 4.0.4 on 2022-04-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supermarket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sup', models.IntegerField()),
                ('name_sup', models.CharField(max_length=20)),
                ('national_num_sup', models.IntegerField()),
                ('phone', models.CharField(max_length=11)),
                ('password_sup', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('city', models.CharField(max_length=250)),
                ('address', models.TextField(blank=True)),
                ('from_hour', models.TimeField(blank=True)),
                ('to_hour', models.TimeField(blank=True)),
                ('owner', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
