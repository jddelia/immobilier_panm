# Generated by Django 2.1.2 on 2018-11-12 23:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.TextField()),
                ('more_photos', models.TextField(blank=True)),
                ('price', models.CharField(max_length=75)),
                ('alt', models.CharField(max_length=100)),
                ('tags', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
