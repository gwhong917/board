# Generated by Django 3.2.8 on 2021-10-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('a_no', models.AutoField(db_column='a_no', primary_key=True, serialize=False)),
                ('a_type', models.CharField(db_column='a_type', max_length=50)),
                ('a_title', models.CharField(db_column='a_title', max_length=255)),
                ('a_note', models.CharField(db_column='a_note', max_length=4096)),
                ('a_image', models.CharField(db_column='a_image', max_length=1000)),
                ('a_count', models.IntegerField(db_column='a_count', default=0)),
                ('a_datetime', models.DateTimeField(db_column='a_datetime')),
                ('a_usage', models.CharField(db_column='a_usage', max_length=10)),
            ],
            options={
                'db_table': 'album',
                'managed': False,
            },
        ),
    ]
