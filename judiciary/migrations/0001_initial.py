# Generated by Django 2.1.7 on 2019-03-25 10:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('middlename', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('mugshot', models.FileField(upload_to='')),
                ('mugshot_no', models.IntegerField()),
                ('fingerprint', models.FileField(upload_to='')),
                ('sentence_date', models.DateTimeField(default=datetime.datetime(2019, 3, 25, 10, 23, 7, 665776, tzinfo=utc))),
                ('felony_description', models.TextField()),
                ('sentencing_description', models.TextField()),
                ('prisonname', models.CharField(max_length=50)),
            ],
        ),
    ]