# Generated by Django 4.2.9 on 2024-02-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(blank=True, max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
