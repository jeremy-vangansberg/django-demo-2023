# Generated by Django 4.1 on 2023-03-21 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, null=True)),
                ('convert', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
