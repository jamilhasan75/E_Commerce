# Generated by Django 5.0.7 on 2024-07-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('subject', models.CharField(max_length=450)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'ContactInformation',
            },
        ),
    ]
