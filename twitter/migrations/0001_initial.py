# Generated by Django 2.1.2 on 2018-10-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_percentage', models.CharField(max_length=10)),
                ('city_name', models.CharField(max_length=100)),
                ('disaster', models.CharField(max_length=20)),
            ],
        ),
    ]
