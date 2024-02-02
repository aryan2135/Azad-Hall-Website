# Generated by Django 4.1.4 on 2023-12-23 15:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azad', '0053_alter_achievements_date_alter_azad_boarders_books_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 23, 20, 44, 7, 823068)),
        ),
        migrations.AlterField(
            model_name='azad_boarders',
            name='books',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='review',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 20, 44, 7, 823068)),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 20, 44, 7, 823068)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 23, 20, 44, 7, 823068)),
        ),
        migrations.AlterField(
            model_name='para',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 23, 20, 44, 7, 823068)),
        ),
    ]
